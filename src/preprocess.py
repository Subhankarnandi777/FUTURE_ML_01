import pandas as pd

def load_data():
    train = pd.read_csv("data/raw/train.csv")
    stores = pd.read_csv("data/raw/stores.csv")
    oil = pd.read_csv("data/raw/oil.csv")
    holidays = pd.read_csv("data/raw/holidays_events.csv")

    train["date"] = pd.to_datetime(train["date"])
    oil["date"] = pd.to_datetime(oil["date"])
    holidays["date"] = pd.to_datetime(holidays["date"])

    df = train.merge(stores, on="store_nbr", how="left")
    df = df.merge(oil, on="date", how="left")
    df = df.merge(holidays, on="date", how="left")

    df["dcoilwtico"] = df["dcoilwtico"].fillna(method="ffill")
    df["holiday_flag"] = df["type_y"].notnull().astype(int)

    return df

if __name__ == "__main__":
    df = load_data()
    df.to_csv("data/processed/merged_data.csv", index=False)