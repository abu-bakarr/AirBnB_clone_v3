#!/usr/bin/python3
"""List of states"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {"amenities": "Amenity",
           "cities": "City",
           "places": "Place",
           "reviews": "Review",
           "states": "State",
           "users": "User"
           }


@app_views.route('/status')
def api_status():
    """api_status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    '''retrieves the number of each objects by type'''
    dict = {}
    for key, value in classes.items():
        dict[key] = storage.count(value)
    return jsonify(dict)
