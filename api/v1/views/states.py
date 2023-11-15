#!/usr/bin/python3
"""Defines a view to handle all default RESTful API actions for State objects.
"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """Retrieves a list of all the state objects of the storage system."""

    state_objects = storage.all(State)  # a dict
    state_list = []
    for state in state_objects.values():
        state_list.append(state.to_dict())

    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE'], strict_slashes=False)
def one_state(state_id):
    """Retrieves or deletes the state object of the specified state_id."""

    state = storage.get(State, state_id)
    if state is None:
        return abort(404)

    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return {}, 200

    return jsonify(state.to_dict())
