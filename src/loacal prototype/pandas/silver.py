from pathlib import Path

def save_silver(df, symbol):

    output_dir = Path("data/silver")

    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / f"{symbol}_clean.parquet"

    df.to_parquet(file_path)

    print(f"Saved Silver Layer: {file_path}")