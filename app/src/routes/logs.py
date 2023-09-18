from controllers.logs import generate_logs
from flask import request, jsonify, Blueprint

log_routes = Blueprint('logs', __name__, url_prefix='/logs')
    
@log_routes.route('/random', methods=['GET'])
def random_logs():
        count = request.args.get('count', default=100, type=int)

        generated_logs = generate_logs(count)
        return jsonify({
            "success": True, 
            "generated_logs": generated_logs
        })