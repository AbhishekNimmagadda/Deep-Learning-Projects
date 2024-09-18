
from flask import Blueprint, request, jsonify, send_file
import numpy as np
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

from app.models import load_trained_model, load_scaler

main = Blueprint('main', __name__)

# Load the trained model and scaler
model = load_trained_model('/home/ec2-user/self_projects/stock_prediction/models/stock_price_prediction_model.h5')

scaler = load_scaler('/home/ec2-user/self_projects/stock_prediction/models/scaler.save')

@main.route('/')
def home():
    return "Welcome to the Stock Price Prediction API!"

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['input']).reshape(-1, 1)  # Reshape for the scaler

    # Assuming the scaler was fit on 2D data, transform the input_data accordingly
    scaled_data = scaler.transform(input_data).reshape(1, -1, 1)

    prediction = model.predict(scaled_data)
    output = scaler.inverse_transform(prediction.reshape(-1, 1)).flatten()
    return jsonify({'prediction': output.tolist()})

@main.route('/plot')
def plot():
    plot_path = '/home/ec2-user/stock_price_prediction/models/stock_price_prediction.png'
    return send_file(plot_path, mimetype='image/png')

@main.route('/client_predict_plot', methods=['POST'])
def client_predict_plot():
    data = request.get_json()
    input_data = np.array(data['input']).reshape(-1, 1)  # Reshape for the scaler

    # Assuming the scaler was fit on 2D data, transform the input_data accordingly
    scaled_data = scaler.transform(input_data).reshape(1, -1, 1)

    prediction = model.predict(scaled_data)
    predictions = scaler.inverse_transform(prediction.reshape(-1, 1)).flatten()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(input_data.flatten(), label='Client Input Data', marker='o', linestyle='-')
    plt.plot(predictions, label='Predictions', marker='o', linestyle='--')
    plt.title('Client Data Prediction')
    plt.xlabel('Time Step')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot as PNG
    plot_path = '/home/ec2-user/self_projects/stock_prediction/client_prediction_plot.png'
    plt.savefig(plot_path)
    plt.close()  # Close the plot to free memory

    # Return the plot as an image file
    return send_file(plot_path, mimetype='image/png')
