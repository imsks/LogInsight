import sys
from flask import Flask, request, jsonify

# Append the 'src' folder to the Python path
sys.path.append('src')

from routes.logs import RandomLogs

app = Flask(__name__)
app.debug = True

# Random Logging
@app.route('/logs/random', methods = ['GET'])
def route():
    method = request.method

    if method == "GET":
        return RandomLogs.logs()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
