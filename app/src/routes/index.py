from flask import request, jsonify, Blueprint

base_routes = Blueprint('base', __name__, url_prefix='/')
    
@base_routes.route('/', methods=['GET'])
def server_status():
    method = request.method

    if method == "GET":
        return jsonify({
            "success": True, 
        })