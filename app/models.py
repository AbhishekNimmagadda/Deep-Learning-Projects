
from tensorflow.keras.models import load_model

import joblib

# need to get fullpath of the model
def load_trained_model(model):
    return load_model(model)


def load_scaler(scaled_model):
    return joblib.load(scaled_model)
