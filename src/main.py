from extract import fetch_stock

from transform import (
    validate,
    clean_columns,
    clean_data,
    create_features
)

from bronze import save_parquet
from silver import save_silver
from gold import save_gold

symbol = "AAPL"

# Extract
df = fetch_stock(symbol)

# Validate
df = validate(df)

# Fix columns
df = clean_columns(df)

# Bronze
save_parquet(df, symbol)

# Silver
silver_df = clean_data(df)

save_silver(silver_df, symbol)

# Gold
gold_df = create_features(silver_df)

save_gold(gold_df, symbol)