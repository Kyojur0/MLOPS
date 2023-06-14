from flask import Flask, render_template, request, jsonify
import pandas as pd
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/test', methods=['POST', 'GET'])
def test():
    # Get the JSON data from the request\
    json_data = request.get_json()

    # Convert the JSON data to a DataFrame
    input_data = {
        'fixed acidity': json_data.get('fixed-acidity'),
        'volatile acidity': json_data.get('volatile-acidity'),
        'citric acid': json_data.get('citric-acid'),
        'residual sugar': json_data.get('residual-sugar'),
        'chlorides': json_data.get('chlorides'),
        'free sulfur dioxide': json_data.get('free-sulfur-dioxide'),
        'total sulfur dioxide': json_data.get('total-sulfur-dioxide'),
        'density': json_data.get('density'),
        'pH': json_data.get('ph'),
        'sulphates': json_data.get('sulphates'),
        'alcohol': json_data.get('alcohol')
    }

    df = pd.DataFrame(input_data, index=[0])

    # Load the model as a PyFunc model
    model = joblib.load('models/model.pkl')

    # Perform prediction using the loaded model
    prediction = model.predict(df)

    # Create a response with the desired output
    output_data = {
        'quality': round(prediction[0])  # Replace '5' with the actual output value
    }

    return jsonify(output_data)

@app.route('/test_get', methods=['POST', 'GET'])
def test_get():
    dict = {
        'name': 'bruh'
    }
    return jsonify(dict)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

