def write_parquet(df, output_path):
    """
    Write Spark DataFrame to Parquet.
    """

    (
        df.write
        .mode("overwrite")
        .parquet(output_path)
    )