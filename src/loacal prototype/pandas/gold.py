from pathlib import Path

def save_gold(df, symbol):

    output_dir = Path("data/gold")

    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / f"{symbol}_features.parquet"

    df.to_parquet(file_path)

    print(f"Saved Gold Layer: {file_path}")