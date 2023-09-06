from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = True

# Sample data (you can use a database in a real application)
data = []

# GET endpoint
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
