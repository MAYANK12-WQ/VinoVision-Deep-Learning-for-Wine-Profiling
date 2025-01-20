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
