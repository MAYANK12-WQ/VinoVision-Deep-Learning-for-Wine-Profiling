# Wine Quality Prediction Using Deep Learning

This project demonstrates the use of deep learning for wine quality prediction using a small dataset from the UCI Machine Learning Repository. It aims to help beginners understand the basics of neural networks and deep learning libraries like Keras, while applying these techniques to real-world data.

## About the Dataset
The dataset contains 12 variables influencing wine quality, including:

- **Fixed Acidity**: Non-volatile acids in wine, expressed in g/dm³.
- **Volatile Acidity**: Indicators of wine spoilage turning into vinegar, in g/dm³.
- **Citric Acid**: A fixed acid contributing to wine freshness, in g/dm³.
- **Residual Sugar**: Remaining sugar after fermentation, in g/dm³.
- **Chlorides**: A contributor to saltiness, in g/dm³.
- **Free Sulfur Dioxide**: Preservative added to wines, in g/dm³.
- **Total Sulfur Dioxide**: Sum of bound and free sulfur dioxide, in g/dm³.

For the full dataset, visit the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/).

## Steps to Build the Deep Learning Model

### Step 1: Know Your Data
Load and explore the wine quality data.

```python
import pandas as pd

# Load data
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')

# Check the data
print(red.head())
print(white.describe())

Step 2: Visualize the Data
Create histograms to visualize the alcohol distribution for red and white wines.

python
Copy
Edit
import matplotlib.pyplot as plt

# Create histograms
fig, ax = plt.subplots(1, 2)
ax[0].hist(red['alcohol'], color='red', alpha=0.5, label='Red Wine')
ax[1].hist(white['alcohol'], color='white', edgecolor='black', alpha=0.5, label='White Wine')

# Set labels
ax[0].set_title("Red Wine Alcohol")
ax[1].set_title("White Wine Alcohol")
plt.show()
Step 3: Split the Data
Combine datasets, add labels, and split them for training and testing.

python
Copy
Edit
# Add labels
red['type'] = 1
white['type'] = 0
wines = pd.concat([red, white], ignore_index=True)

# Split data
from sklearn.model_selection import train_test_split
X = wines.iloc[:, :-1]
y = wines['type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.34, random_state=42)
Step 4: Build the Neural Network
Define and compile a deep learning model using Keras.

python
Copy
Edit
from keras.models import Sequential
from keras.layers import Dense

# Define model
model = Sequential([
    Dense(12, activation='relu', input_shape=(11,)),
    Dense(9, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
Step 5: Train and Evaluate the Model
Train the model and evaluate its performance.

python
Copy
Edit
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# Evaluate
accuracy = model.evaluate(X_test, y_test)[1]
print(f"Model Accuracy: {accuracy}")
Project Features
Wine Classification: Classify wine as red or white based on chemical properties.
Visualization: Create histograms for data exploration.
Deep Learning: Build a neural network for binary classification.
Keras: Use Keras for model definition, training, and evaluation.
Requirements
Install the required dependencies using:

bash
Copy
Edit
pip install pandas numpy matplotlib scikit-learn keras tensorflow
Contributing
Contributions are welcome! Fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Data sourced from the UCI Machine Learning Repository.

vbnet
Copy
Edit

You can copy-paste this as your **README.md** file. It’s formatted for GitHub and includes all
