# 🚀 AlphaPipeline
## End-to-End Cloud Data Engineering Pipeline using Microsoft Azure

---

## 📌 Project Overview

AlphaPipeline is an end-to-end Cloud Data Engineering project that demonstrates how raw financial market data is transformed into analytics-ready datasets using Microsoft's Azure ecosystem.

The project implements the **Medallion Architecture (Bronze → Silver → Gold)** using **Azure Data Lake Storage Gen2**, **Azure Databricks**, and **Azure Data Factory** to automate the ETL workflow.

The processed Gold layer will later be used for **Machine Learning-based stock prediction** and deployed as a complete cloud application.

---

# 🏗️ Project Methodology

![Project Methodology](architecture/methodology.png)
---

# ☁️ Final Azure Architecture

```
Yahoo Finance
        │
        ▼
Azure Data Lake Storage Gen2
(Bronze Layer)
        │
        ▼
Azure Databricks
(Bronze → Silver)
        │
        ▼
Azure Data Lake Storage Gen2
(Silver Layer)
        │
        ▼
Azure Databricks
(Silver → Gold)
        │
        ▼
Azure Data Lake Storage Gen2
(Gold Layer)
        │
        ▼
Azure Data Factory
(Pipeline Orchestration)
        │
        ▼
Machine Learning (Coming Soon)
        │
        ▼
Deployment (Coming Soon)
```

---

# 🛠️ Technology Stack

## Cloud Services

- Microsoft Azure
- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Data Factory

## Programming Language

- Python
- PySpark

## Data Source

- Yahoo Finance (yfinance)

## Storage Format

- Parquet

## Architecture

- ETL Pipeline
- Medallion Architecture
- Data Validation
- Feature Engineering

---

# 📂 Project Workflow

## Step 1 — Data Ingestion

Financial stock market data is collected from Yahoo Finance.

The raw dataset is uploaded into the **Bronze container** inside Azure Data Lake Storage Gen2.

---

## Step 2 — Bronze Layer

The Bronze layer stores the raw, unprocessed dataset.

Example:

```
AAPL_20260702.parquet
```

No transformations are applied in this layer.

---

## Step 3 — Bronze → Silver

Executed using Azure Databricks Notebook:

```
bronze_to_silver
```

Operations performed:

- Read Bronze data
- Remove duplicate records
- Remove null values
- Validate schema
- Validate data quality
- Write cleaned dataset into Silver Layer

Output:

```
AAPL_clean.parquet
```

---

## Step 4 — Silver Layer

The Silver layer stores cleaned and validated data.

This layer becomes the input for feature engineering.

---

## Step 5 — Silver → Gold

Executed using Azure Databricks Notebook:

```
silver_to_gold
```

Feature Engineering:

- Daily Return
- Moving Average (MA5)
- Moving Average (MA20)
- Volatility

Output:

```
AAPL_features.parquet
```

---

## Step 6 — Gold Layer

The Gold layer stores analytics-ready datasets.

This data is prepared for:

- Machine Learning
- Dashboarding
- Reporting
- Prediction

---

## Step 7 — Azure Data Factory

Azure Data Factory orchestrates the complete ETL workflow.

Pipeline:

```
bronze_to_silver
        │
        ▼
silver_to_gold
```

Pipeline Activities

- Notebook Activity
- Linked Service
- Access Token Authentication
- Success Dependency
- Validate Pipeline
- Publish Pipeline
- Debug Pipeline

Once executed, Azure Data Factory automatically performs the complete ETL workflow from Bronze to Gold.

---

# 🥉🥈🥇 Medallion Architecture

| Layer | Purpose |
|--------|----------|
| Bronze | Raw data storage |
| Silver | Cleaned and validated data |
| Gold | Feature engineered analytics-ready data |

---

# 📁 Project Structure

```
AlphaPipeline
│
├── architecture/
│   └── methodology.png
│
├── reports/
│
├── src/
│   │
│   ├── azure/
│   │   ├── bronze_to_silver.ipynb
│   │   └── silver_to_gold.ipynb
│   │
│   └── local_prototype/
│       ├── pandas/
│       └── pyspark/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ✅ Completed Features

- Azure Resource Group
- Azure Data Lake Storage Gen2
- Azure Databricks Workspace
- Azure Compute Cluster
- Azure Data Factory
- Medallion Architecture
- Bronze Layer
- Silver Layer
- Gold Layer
- Data Validation
- Duplicate Removal
- Null Handling
- Feature Engineering
- Pipeline Orchestration

---

# 📈 Machine Learning

🚧 **This section will be completed in Phase 7.**

---

# 🌐 Deployment

🚧 **This section will be completed in Phase 8.**

---

# 🔄 Project Evolution

This project was intentionally developed in multiple stages.

1. Local ETL prototype using **Pandas**
2. Distributed processing prototype using **PySpark**
3. Final cloud implementation using:

- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Data Factory

The local implementations are preserved inside:

```
src/local_prototype/
```

The Azure implementation represents the final architecture of this project.

---

# 📬 Contact

**Rakesh Kumar**

B.Tech Computer Science Engineering

Cloud Data Engineering | Machine Learning | Azure
