from pyspark.sql.functions import col, count, when


def validate_data(df):
    """
    Perform basic data quality checks.
    """

    print("\n=== Total Rows ===")
    print(df.count())

    print("\n=== Duplicate Rows ===")
    print(df.count() - df.dropDuplicates().count())

    print("\n=== Null Values ===")

    null_df = df.select([
        count(when(col(c).isNull(), c)).alias(c)
        for c in df.columns
    ])

    null_df.show()

    print("\n=== Schema ===")
    df.printSchema()