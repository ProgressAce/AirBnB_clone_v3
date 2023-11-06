#!/usr/bin/python3
"""Setup api endpoints."""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """displays a status message."""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def object_count():
    """displays the number of objects by type."""

    types = {
            "amenities": Amenity,
            "cities": City,
            "places": Place,
            "reviews": Review,
            "states": State,
            "users": User
            }

    object_count = {}
    for t, cls in types.items():
        count = storage.count(cls)
        object_count[t] = count

    return jsonify(object_count)
