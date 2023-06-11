from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a sample route
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
