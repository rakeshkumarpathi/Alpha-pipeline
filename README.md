# AlphaPipeline

AlphaPipeline is an end-to-end financial data engineering project that collects stock market data, processes it using a Medallion Architecture, stores analytics-ready data in PostgreSQL, performs analytics and data quality checks, and uses PySpark for distributed data processing.

## Architecture

Yahoo Finance  
↓  
Data Ingestion  
↓  
Bronze Layer (Raw Data)  
↓  
Silver Layer (Cleaned Data)  
↓  
Gold Layer (Feature-Engineered Data)  
↓  
PostgreSQL Data Warehouse  
↓  
Analytics & Data Quality  
↓  
PySpark Processing  
↓  
Processed Parquet Output  

## Phase 1 – Data Ingestion

- Extracted stock market data using Yahoo Finance.
- Built a Python-based ETL pipeline.
- Stored raw stock data in Parquet format.

## Phase 2 – Medallion Architecture

Implemented Bronze, Silver, and Gold data layers.

**Bronze Layer**
- Stores raw stock market data.

**Silver Layer**
- Data cleaning.
- Duplicate removal.
- Null handling.

**Gold Layer**
- Analytics-ready data.
- Feature engineering.

Engineered features:

- MA_5
- MA_20
- Daily Return
- Volatility

## Phase 3 – Data Warehouse

- PostgreSQL data warehouse.
- Schema mapping and validation.
- Parquet to PostgreSQL loading.
- SQLAlchemy database connectivity.
- Full-refresh loading strategy.

## Phase 4 – Analytics Layer

- SQL analytics queries.
- Business KPIs.
- Data quality reports.
- Console analytics dashboard.
- Stock price visualizations.
- Moving average analysis.
- Trading volume analysis.
- Daily return analysis.
- Volatility analysis.
- Combined dashboard visualization.

## Phase 5 – Distributed Data Processing with PySpark

- Created and configured SparkSession.
- Read Parquet datasets using Spark.
- Used Spark DataFrames for distributed processing.
- Implemented Spark transformations.
- Executed analytical queries using Spark SQL.
- Performed distributed data validation.
- Inspected Spark DataFrame schemas.
- Used caching and persistence concepts.
- Learned partition management using `repartition()` and `coalesce()`.
- Inspected Spark execution plans using `explain()`.
- Wrote processed Spark DataFrames back to Parquet format.

## WSL and Linux Development Environment

PySpark was executed inside Windows Subsystem for Linux (WSL2) using Ubuntu to provide a Linux-based Spark development environment.

The environment includes:

- WSL2 with Ubuntu.
- OpenJDK 17 for running Apache Spark.
- Python virtual environment for dependency isolation.
- PySpark 4.1.2.
- Hadoop 3.4.2 runtime used by Spark.
- Linux-based execution of Spark pipelines.
- Parquet reading and writing through Spark.
- Separate Windows development and Git workflow with WSL used as the PySpark execution environment.

The project code is maintained in the Windows project directory and synchronized with the WSL environment when running and testing PySpark pipelines.

## Pandas vs PySpark

| Pandas | PySpark |
|---|---|
| Single-machine processing | Distributed processing |
| Suitable for small and medium datasets | Designed for large datasets |
| Eager execution | Lazy execution |
| Uses local system memory | Can distribute processing across multiple machines |
| Simple local DataFrames | Distributed Spark DataFrames |

## Tech Stack

- Python
- Pandas
- PySpark
- Apache Spark
- PostgreSQL
- SQLAlchemy
- Parquet
- Yahoo Finance API
- Matplotlib
- Git
- GitHub
- WSL2
- Ubuntu Linux
- Java 17

## Project Structure

    Alpha-Pipeline/
    ├── config/
    ├── data/
    │   ├── bronze/
    │   ├── silver/
    │   ├── gold/
    │   └── spark_output/
    ├── reports/
    ├── src/
    │   ├── extract.py
    │   ├── transform.py
    │   ├── bronze.py
    │   ├── silver.py
    │   ├── gold.py
    │   ├── warehouse.py
    │   ├── load_warehouse.py
    │   ├── analytics.py
    │   ├── queries.py
    │   ├── quality.py
    │   ├── dashboard.py
    │   ├── visualization.py
    │   ├── spark_session.py
    │   ├── spark_read.py
    │   ├── spark_transform.py
    │   ├── spark_validation.py
    │   ├── spark_write.py
    │   ├── spark_main.py
    │   └── main.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md