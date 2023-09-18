from flask import request, jsonify
from utils.log_generator import generate_random_logs

# Handle GET
def get_handler():
    return jsonify({
        'status': True
    })

# Handle POST
def post_handler():
    return jsonify({
        'status': True
    })