# model_training.py
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np

def build_and_train_model(data):
    # Split data
    X = data.iloc[:, :-1]
    y = data['type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.34, random_state=42)

    # Build model
    model = Sequential([
        Dense(12, activation='relu', input_shape=(11,)),
        Dense(9, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train model
    model.fit(X_train, y_train, epochs=10, batch_size=16, verbose=1)
    accuracy = model.evaluate(X_test, y_test)[1]
    print(f"Model Accuracy: {accuracy}")

    return model
