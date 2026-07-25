from pyspark.sql.functions import col


def transform_data(df):
    """
    Perform basic Spark transformations.
    """

    # Select only required columns
    transformed_df = (
        df.select(
            "Date",
            "Close",
            "Volume",
            "Daily_Return"
        )
        .filter(col("Close") > 250)
        .orderBy(col("Date"))
    )

    return transformed_df