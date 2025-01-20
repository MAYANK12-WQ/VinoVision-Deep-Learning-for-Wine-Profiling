# data_preprocessing.py
import pandas as pd

def load_and_clean_data():
    # Load datasets
    red = pd.read_csv("data/winequality-red.csv", sep=";")
    white = pd.read_csv("data/winequality-white.csv", sep=";")
    
    # Add labels
    red['type'] = 1
    white['type'] = 0
    
    # Concatenate datasets
    wines = pd.concat([red, white], ignore_index=True)
    
    # Check for null values
    if wines.isnull().sum().sum() > 0:
        wines = wines.dropna()
    
    return wines
