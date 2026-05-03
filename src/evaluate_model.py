import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_csv("data/processed/cleaned_data.csv")

X = df.drop(columns=["sales", "date", "family"])
y = df["sales"]

X = pd.get_dummies(X, drop_first=True)

split_idx = int(len(X) * 0.8)

X_test = X.iloc[split_idx:]
y_test = y.iloc[split_idx:]

model = joblib.load("models/xgboost_model.pkl")

preds = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("RMSE:", np.sqrt(mean_squared_error(y_test, preds)))
print("R2:", r2_score(y_test, preds))