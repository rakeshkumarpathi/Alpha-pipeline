def validate(df):

    print("\nRunning validation...\n")

    # Check empty dataframe
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Check null values
    null_count = df.isnull().sum().sum()

    if null_count > 0:
        print(f"Warning: {null_count} null values found")

    # Check duplicates
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        print(f"Warning: {duplicates} duplicate rows found")

    print("Validation successful")

    return df

def clean_columns(df):

    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)
    df.columns.name = None
    return df

def clean_data(df):

    print("\nCleaning data...\n")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove null values
    df = df.dropna()

    return df
def create_features(df):

    print("\nCreating Gold Layer Features...\n")

    # Short-term trend
    df["MA_5"] = df["Close"].rolling(window=5).mean()

    # Long-term trend
    df["MA_20"] = df["Close"].rolling(window=20).mean()

    # Daily percentage change
    df["Daily_Return"] = df["Close"].pct_change()

    # Risk measurement
    df["Volatility"] = (
        df["Daily_Return"]
        .rolling(window=5)
        .std()
    )

    return df