import pandas as pd
from datetime import datetime

def write_silver(df, silver_dir):
    for date, group in df.groupby("signup_date"):
        path = silver_dir / f"signup_date={date}"
        path.mkdir(parents=True, exist_ok=True)
        group.to_parquet(path / f"part-{datetime.now().timestamp()}.parquet", index=False)

def write_quarantine(df, quarantine_dir, file_name):
    if len(df) == 0:
        return
    today = datetime.now().strftime("%Y-%m-%d")
    path = quarantine_dir / today
    path.mkdir(parents=True, exist_ok=True)
    df.to_csv(path / f"{file_name}_rejected.csv", index=False)