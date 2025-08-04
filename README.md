# 📊 Databricks Declarative Pipelines with Delta Live Tables (DLT)

This project demonstrates a **production-grade data pipeline** built using **Databricks Delta Live Tables (DLT)** — a fully managed, declarative ETL framework for building reliable, maintainable data pipelines at scale.

## 🚀 Key Features

- 🔁 **Delta Live Tables (DLT)**: Declarative pipeline using SQL and PySpark for automatic lineage, orchestration, and quality checks.
- 🔄 **Slowly Changing Dimensions (SCD)**:
  - **Type 1** – Overwrites old data with new values for changed records.
  - **Type 2** – Preserves historical data by tracking changes over time using surrogate keys and timestamps.
- 📈 **Monitoring & Observability**:
  - Built-in data quality checks with DLT expectations.
  - DLT UI for pipeline status, event logs, and lineage visualization.
- 🚨 **Alerts & Notifications**:
  - Integration with Databricks Jobs and alerting tools for pipeline failures or data quality violations.

## 🏗️ Architecture Overview


        ┌─────────────┐
        │ Raw Sources │
        └─────┬───────┘
              ▼
     ┌────────────────────┐
     │ Bronze DLT Table   │  ← Raw ingestion
     └────────┬───────────┘
              ▼
     ┌────────────────────┐
     │ Silver DLT Table   │  ← SCD logic applied
     └────────┬───────────┘
              ▼
     ┌────────────────────┐
     │ Gold DLT Table     │  ← Analytics-ready
     └────────────────────┘


## 📂 Project Structure

├── notebooks/
│ ├── 01_bronze_dlt.py
│ ├── 02_silver_scd_type1.py
│ ├── 03_silver_scd_type2.py
│ └── 04_gold_tables.py
├── config/
│ └── expectations.json # Data quality rules
├── alerts/
│ └── dlt_failure_alerts.json # Notification configs
├── README.md
└── requirements.txt



## ⚙️ Technologies Used

- 🧱 **Databricks**
- ⚡ **Delta Live Tables**
- 🐍 **PySpark / Spark SQL**
- 📜 **Delta Lake**
- 📬 **Webhooks / Alerting Tools**
- 📊 **Unity Catalog** (optional)

## 🧪 Data Quality & Expectations

DLT Expectations are defined to:

- Ensure primary key uniqueness
- Detect nulls in critical columns
- Validate schema and value constraints

Failing expectations can either drop bad records or halt the pipeline based on severity.

## 🔔 Alerts & Monitoring

- Integrated alerting on DLT pipeline failure or anomalies
- Logs available via the DLT UI and Databricks workspace
- Optionally send notifications to Slack, Teams, or Email using webhooks

## 📈 Use Cases

This project is ideal for:

- Implementing change data capture (CDC) logic in batch/streaming pipelines
- Building Type 1 and Type 2 dimension tables
- Observing and alerting on production data quality issues

## 📝 Future Enhancements

- Add unit tests with `pytest`
- CI/CD deployment via Databricks CLI or Terraform
- Integration with Unity Catalog for fine-grained access control

## 🧠 Learn More

- [Delta Live Tables Documentation](https://docs.databricks.com/data-engineering/delta-live-tables/index.html)
- [SCD Type 1 vs Type 2](https://www.datawarehouse4u.info/SCD-Slowly-Changing-Dimension.html)
