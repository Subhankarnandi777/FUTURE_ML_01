import pandas as pd
import joblib


test = pd.read_csv("data/raw/test.csv")
stores = pd.read_csv("data/raw/stores.csv")
oil = pd.read_csv("data/raw/oil.csv")

test["date"] = pd.to_datetime(test["date"])
oil["date"] = pd.to_datetime(oil["date"])


df = test.merge(stores, on="store_nbr", how="left")
df = df.merge(oil, on="date", how="left")


df["dcoilwtico"] = df["dcoilwtico"].ffill()

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["dayofweek"] = df["date"].dt.dayofweek
df["quarter"] = df["date"].dt.quarter
df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)

df["lag_1"] = 0
df["lag_7"] = 0
df["rolling_mean_7"] = 0

X_forecast = df.drop(columns=["date", "family", "id"])

X_forecast = pd.get_dummies(X_forecast, drop_first=True)


train_cols = joblib.load("models/feature_columns.pkl")

for col in train_cols:
    if col not in X_forecast.columns:
        X_forecast[col] = 0

X_forecast = X_forecast[train_cols]

model = joblib.load("models/xgboost_model.pkl")


df["predicted_sales"] = model.predict(X_forecast)


forecast_output = df[
    ["id", "date", "store_nbr", "family", "predicted_sales"]
]

forecast_output.to_csv(
    "data/processed/forecast_output.csv",
    index=False
)

print("Forecast generated successfully.")