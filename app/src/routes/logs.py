from controllers.logs import generate_logs
from flask import request, jsonify

class RandomLogs():
    def logs():
        count = request.args.get('count', default=100, type=int)

        generated_logs = generate_logs(count)
        return jsonify({
            "success": True, 
            "generated_logs": generated_logs
        })