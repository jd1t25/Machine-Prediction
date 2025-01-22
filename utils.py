from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import classification_report

import pandas as pd
import numpy as np

# Model Trainer class
class ModelTrainer:
    def __init__(self):
        self.gbc = None

    def preprocess_data(self, df: pd.DataFrame):
        """Preprocess the data: handle missing values and encode categorical features."""
        df = df.dropna()

        # Initialize LabelEncoder
        le = LabelEncoder()
        for column in df.columns:
            if df[column].dtype == type(object):
                df[column] = le.fit_transform(df[column])

        return df

    def train(self, df: pd.DataFrame) -> dict:
        """Train the Gradient Boosting model."""
        # Preprocess the data
        df = self.preprocess_data(df)

        # Split features (X) and target (y)
        X = df.drop(['Downtime'], axis=1)
        y = df['Downtime']

        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

        # Initialize and train the model
        self.gbc = GradientBoostingClassifier()
        self.gbc.fit(X_train, y_train)

        # Make predictions and get the classification report
        y_pred = self.gbc.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)

        # Return the classification report
        return report

    def predict(self, features: np.array) -> np.array:
        """Make predictions using the trained model."""
        if self.gbc is None:
            raise ValueError("Model has not been trained yet. Please train the model first.")
        
        # Make predictions using the trained model (self.gbc)
        return self.gbc.predict(features)