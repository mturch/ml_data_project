"""
Data utility functions for loading, cleaning, and preprocessing data.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data(filepath):
    """
    Load data from various file formats.
    
    Args:
        filepath (str): Path to the data file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format")


def basic_info(df):
    """
    Display basic information about the dataset.
    
    Args:
        df (pd.DataFrame): Input dataframe
    """
    print(f"Dataset shape: {df.shape}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nBasic statistics:\n{df.describe()}")


def handle_missing_values(df, strategy='drop'):
    """
    Handle missing values in the dataset.
    
    Args:
        df (pd.DataFrame): Input dataframe
        strategy (str): Strategy for handling missing values ('drop', 'fill_mean', 'fill_median')
        
    Returns:
        pd.DataFrame: Processed dataframe
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill_mean':
        return df.fillna(df.mean())
    elif strategy == 'fill_median':
        return df.fillna(df.median())
    else:
        raise ValueError("Invalid strategy")


def encode_categorical(df, columns=None):
    """
    Encode categorical variables.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of columns to encode (if None, auto-detect)
        
    Returns:
        pd.DataFrame: Encoded dataframe
    """
    if columns is None:
        columns = df.select_dtypes(include=['object']).columns
    
    df_encoded = df.copy()
    for col in columns:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df[col])
    
    return df_encoded