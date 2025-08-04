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

