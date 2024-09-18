
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def preprocess_data(file_path, seq_length=60):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')
    data = data.set_index('Date')
    data = data[['Close']]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    
    def create_sequences(data, seq_length):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            y.append(data[i+seq_length])
        return np.array(X), np.array(y)
    
    X, y = create_sequences(scaled_data, seq_length)
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    return X_train, X_test, y_train, y_test, scaler

if __name__ == "__main__":

    file_path = '/home/ec2-user/self_projects/stock_prediction/data/raw/Meta_Dataset.csv'
    X_train, X_test, y_train, y_test, scaler = preprocess_data(file_path)
    
    # Save the processed data for model training
    np.save('/home/ec2-user/self_projects/stock_prediction/data/processed/X_train.npy', X_train)
    np.save('/home/ec2-user/self_projects/stock_prediction/data/processed/X_test.npy', X_test)
    np.save('/home/ec2-user/self_projects/stock_prediction/data/processed/y_train.npy', y_train)
    np.save('/home/ec2-user/self_projects/stock_prediction/data/processed/y_test.npy', y_test)
    
    import joblib
    joblib.dump(scaler, '/home/ec2-user/self_projects/stock_prediction/models/scaler.save')
