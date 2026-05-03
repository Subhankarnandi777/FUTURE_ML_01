import pandas as pd
import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# Load Processed Data
df = pd.read_csv("data/processed/cleaned_data.csv")

# Separate Features and Target
X = df.drop(columns=["sales", "date", "family"])
y = df["sales"]

# One-Hot Encode Categorical Variables
X = pd.get_dummies(X, drop_first=True)

# Save Feature Columns for Forecast Alignment
joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")

# Train/Test Split (No Shuffle for Time Series)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Initialize Model
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8
)

# Train Model
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "models/xgboost_model.pkl")

print("Model and feature columns saved successfully.")