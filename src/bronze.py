from pathlib import Path
from datetime import datetime


def save_parquet(df, symbol):

    output_dir = Path("data/bronze")

    output_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y%m%d")

    file_name = f"{symbol}_{today}.parquet"

    file_path = output_dir / file_name

    df.to_parquet(file_path)

    print(f"Saved to {file_path}")