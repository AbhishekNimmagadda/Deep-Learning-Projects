import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import joblib

def plot_predictions(model, X_test, y_test, scaler):
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    
    plt.figure(figsize=(16, 8))
    plt.plot(predictions, color='red', label='Predicted Prices')
    plt.plot(scaler.inverse_transform(y_test.reshape(-1, 1)), color='blue', label='Actual Prices')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.savefig('/home/ec2-user/self_projects/stock_prediction/models/stock_price_prediction.png')  # Save the plot as a PNG file
    plt.show()

if __name__ == "__main__":
    X_test = np.load('/home/ec2-user/self_projects/stock_prediction/data/processed/X_test.npy')
    y_test = np.load('/home/ec2-user/self_projects/stock_prediction/data/processed/y_test.npy')
    scaler = joblib.load('/home/ec2-user/self_projects/stock_prediction/models/scaler.save')
    
    model = load_model('/home/ec2-user/self_projects/stock_prediction/models/stock_price_prediction_model.h5')
    plot_predictions(model, X_test, y_test, scaler)
