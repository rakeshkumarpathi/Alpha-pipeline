from pyspark.sql import DataFrame


def read_gold_data(spark, file_path: str) -> DataFrame:
    """
    Read Gold Layer Parquet file using Spark.
    """

    df = spark.read.parquet(file_path)

    return df