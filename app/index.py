import sys
from flask import Flask, request, jsonify

# Append the 'src' folder to the Python path
sys.path.append('src')

from routes.index import base_routes
from routes.logs import log_routes

# App Setup
app = Flask(__name__)
app.debug = True

# Register Routes
app.register_blueprint(base_routes)
app.register_blueprint(log_routes)

# App Run Setup
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
