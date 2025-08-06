# 🔁 StreamDLT: A Declarative CDC Pipeline with Delta Live Tables

## 🚀 Overview

**StreamDLT** is a modular and scalable end-to-end data pipeline built using **Databricks Delta Live Tables (DLT)**, designed to simulate a real-world retail environment with multiple branches ("East" and "West") and a product/customer master data system.

The project uses the **Medallion Architecture (Bronze → Silver → Gold)** and demonstrates how to implement **Streaming Ingestion**, **Change Data Capture (CDC)**, and **Slowly Changing Dimensions (SCD Type 1 and Type 2)** declaratively.

---

## 📁 Project Structure

DLT_Pipeline/
├── source_code_transformations/
│ ├── bronze/
│ │ ├── sales_ingestion.py
│ │ ├── products_ingestion.py
│ │ └── customers_ingestion.py
│ ├── silver/
│ │ ├── sales_enr.py
│ │ ├── transformed_products.py
│ │ └── transformed_customers.py
│ └── gold/
│ ├── dim_products.py
│ ├── dim_customers.py
│ ├── fact_sales.py
│ └── business_sales.py
├── DWH_source.sql
└── README.md

---

## 🧱 Architecture

---


---

## 🛠️ Technologies

- **Databricks Delta Live Tables (DLT)**
- **Spark Structured Streaming**
- **PySpark**
- **Delta Lake (ACID Tables)**
- **Medallion Architecture**
- **SCD Type 1 and Type 2**
- **Materialized Views**
- **Streaming Views**
- **Data Quality Expectations**

---

## 🔄 Bronze Layer: Ingestion & Quality Rules

### ✅ Ingested Streaming Tables:
- `sales_stg`: Unified sales data from `sales_east` and `sales_west`.
- `products_stg`, `customers_stg`: Master data from respective source tables.

### ✅ Data Quality with Expectations:
- Applied `@dlt.expect_all_or_drop` for basic checks:
  - `product_id IS NOT NULL`, `price >= 0`
  - `customer_id IS NOT NULL`, `customer_name IS NOT NULL`

---

## 🧪 Silver Layer: Transformations & CDC (Type 1)

### ✅ Key Logic:
- Created **views** (`*_enr_view`) with added business logic (e.g., calculated columns, name formatting).
- Used `dlt.create_auto_cdc_flow()` for **SCD Type 1** to handle changes without history.

### ❗Note:
- Streaming **views** are used to feed downstream Gold layers to avoid issues with upserted streaming tables.

---

## 🪙 Gold Layer: Dimensional Modeling & Aggregates

### 📦 `dim_products`, `dim_customers`
- Built with **SCD Type 2** logic to preserve history.
- Used `stored_as_scd_type = 2` in `create_auto_cdc_flow()`.

### 📊 `fact_sales`
- Upserted with **SCD Type 1** (no history).
- Designed to align with best practices (no SCD 2 on fact tables).

### 📈 `business_sales1`
- A **materialized view** joining fact and dimension tables.
- Aggregates total sales by `region` and `category`.
- Guarantees accurate results across all historical data.

---

## 🔁 CDC Simulation: SQL Inserts

Data changes are simulated in `DWH_source.sql`:
- New sales records (incremental inserts)
- Product price & name changes
- Customer region & name corrections

These updates trigger auto-upserts and history tracking in the pipeline.

---

## ✅ Key Takeaways

- 📌 **DLT enables simplified orchestration** without external schedulers.
- 🛡️ **Expectations enforce data quality** early in the pipeline.
- 🔁 **CDC + SCD logic** supports realistic business scenarios (corrections, updates).
- ⚙️ **Streaming views** solve challenges with upserted streaming tables.
- 📊 **Materialized views** ensure consistent business aggregations.

---

## 🚦 How to Use / Run

1. Load the `DWH_source.sql` data into your Databricks SQL environment.
2. Deploy the pipeline by referencing `source_code_transformations/` in DLT.
3. Run a dry test to validate streaming append logic.
4. Validate CDC handling with incremental inserts (see DWH_source.sql).
5. Visualize results via dashboards or queries on `business_sales1`.

---

## Monitoring

In the jobs and pipeline area of databricks under development tab of your pipeline you can monitor your pipeline.
- configure alerts
- schedule the pipeline
- monitor runs

---

## 📌 Final Notes

This project demonstrates how to simulate a modern retail data pipeline using declarative constructs, without writing complex orchestration code. The modular design makes it easy to extend with more branches, business domains, or additional validations.

---

## 🙌 Acknowledgements

Built using:
- Databricks Delta Live Tables
- Apache Spark
- PySpark and SQL
- Realistic retail business logic

---

## 🧠 Learn More

- [Delta Live Tables Documentation](https://docs.databricks.com/data-engineering/delta-live-tables/index.html)
- [SCD Type 1 vs Type 2](https://www.datawarehouse4u.info/SCD-Slowly-Changing-Dimension.html)
