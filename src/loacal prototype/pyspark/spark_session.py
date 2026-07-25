from pyspark.sql import SparkSession


def create_spark_session():
    """
    Create and return a SparkSession.
    """

    spark = (
        SparkSession.builder
        .appName("AlphaPipeline")
        .master("local[*]")
        .getOrCreate()
    )

    return spark