import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# Load datasets
red = pd.read_csv("data/winequality-red.csv", sep=";")
white = pd.read_csv("data/winequality-white.csv", sep=";")

# Add labels
red['type'] = 1
white['type'] = 0
wines = pd.concat([red, white], ignore_index=True)

# Split data
X = wines.iloc[:, :-1]
y = wines['type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.34, random_state=42)

# Build the model
model = Sequential([
    Dense(12, activation='relu', input_shape=(11,)),
    Dense(9, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=3, batch_size=1, verbose=1)

# Evaluate the model
accuracy = model.evaluate(X_test, y_test)[1]
print(f"Model Accuracy: {accuracy}")

# Visualize alcohol distribution
fig, ax = plt.subplots(1, 2)
ax[0].hist(red['alcohol'], color='red', alpha=0.5, label='Red Wine')
ax[1].hist(white['alcohol'], color='white', edgecolor='black', alpha=0.5, label='White Wine')
ax[0].set_title("Red Wine Alcohol")
ax[1].set_title("White Wine Alcohol")
plt.show()
