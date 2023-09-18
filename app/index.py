import sys
from flask import Flask, request

# Append the 'src' folder to the Python path
sys.path.append('src')

from controllers.index import get_handler, post_handler

# App Setup
app = Flask(__name__)
app.debug = True

@app.route('/logs', methods=['GET', 'POST'])
def random_logs():
    method = request.method

    if method == "GET":
        return get_handler()
    if method == "POST":
        return post_handler()

# App Run Setup
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
