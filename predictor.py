import pandas as pd
import mlflow.pyfunc

# Set the tracking URI to the MLflow server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Define the run ID
run_id = "bdf50f5b3d4d4762a306d5733ed9ba26"

# Load the model as a PyFunc model
model = mlflow.pyfunc.load_model(f"runs:/{run_id}/model")

# Define the input data for prediction
input_data = {
    'fixed acidity': [7.4],
    'volatile acidity': [0.7],
    'citric acid': [0],
    'residual sugar': [1.9],
    'chlorides': [0.076],
    'free sulfur dioxide': [11],
    'total sulfur dioxide': [34],
    'density': [0.9978],
    'pH': [3.51],
    'sulphates': [0.56],
    'alcohol': [9.4],
}

# convert it into dataframe 
df = pd.DataFrame(input_data)

# Perform prediction using the loaded model
prediction = model.predict(df)
print(prediction)
