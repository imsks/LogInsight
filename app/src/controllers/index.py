from flask import request, jsonify
from utils.log_generator import generate_random_logs
from db.indexing import create_mapping

# Handle GET
def get_handler():
    return jsonify({
        'status': True
    })

# Handle POST
def post_handler():
    # Random logs
    logs = generate_random_logs()
    map = create_mapping()

    return jsonify({
        'status': True,
        'map': map
    })