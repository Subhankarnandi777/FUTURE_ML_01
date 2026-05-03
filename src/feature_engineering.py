import pandas as pd

def create_features(df):
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["dayofweek"] = df["date"].dt.dayofweek
    df["quarter"] = df["date"].dt.quarter
    df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)

    df = df.sort_values("date")

    df["lag_1"] = df["sales"].shift(1)
    df["lag_7"] = df["sales"].shift(7)
    df["rolling_mean_7"] = df["sales"].rolling(7).mean()

    df = df.dropna()

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/processed/merged_data.csv", parse_dates=["date"])
    df = create_features(df)
    df.to_csv("data/processed/cleaned_data.csv", index=False)