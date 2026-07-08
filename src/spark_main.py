from spark_session import create_spark_session
from spark_read import read_gold_data
from spark_transform import transform_data
from spark_validation import validate_data
from spark_write import write_parquet


def main():

    spark = create_spark_session()

    try:
        # 1. Read Gold data
        df = read_gold_data(
            spark,
            "data/gold/AAPL_features.parquet"
        )

        # 2. Spark SQL
        df.createOrReplaceTempView("stock_data")

        result_df = spark.sql("""
            SELECT
                Date,
                Close,
                Volume,
                MA_5,
                MA_20
            FROM stock_data
            WHERE Close > 250
            ORDER BY Date
        """)

        print("\n=== Spark SQL Result ===")
        result_df.show(10)

        # 3. Spark transformations
        transformed_df = transform_data(df)

        # Cache because DataFrame is reused
        transformed_df.cache()
        transformed_df.count()

        print("\n=== Transformed Data ===")
        transformed_df.show(10)

        # 4. Validate
        validate_data(transformed_df)

        # 5. Reduce partitions for small local output
        output_df = transformed_df.coalesce(1)

        # 6. Write processed data
        write_parquet(
            output_df,
            "data/spark_output/AAPL_processed"
        )

        print("\nSpark processed data written successfully.")

        transformed_df.unpersist()

    finally:
        spark.stop()


if __name__ == "__main__":
    main()