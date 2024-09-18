import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(X_train, y_train, X_test, y_test):
    model = build_model((X_train.shape[1], 1))
    model.fit(X_train, y_train, batch_size=1, epochs=1)
    model.save('/home/ec2-user/self_projects/stock_prediction/models/stock_price_prediction_model.h5')
    return model

if __name__ == "__main__":
    X_train = np.load('/home/ec2-user/self_projects/stock_prediction/data/processed/X_train.npy')
    y_train = np.load('/home/ec2-user/self_projects/stock_prediction/data/processed/y_train.npy')
    X_test = np.load('/home/ec2-user/self_projects/stock_prediction/data/processed/X_test.npy')
    y_test = np.load('/home/ec2-user/self_projects/stock_prediction/data/processed/y_test.npy')
    
    
    model = train_model(X_train, y_train, X_test, y_test)
