# retail-gcp-analytics-platform
# 🛒 Retail Data Analytics Platform on Google Cloud Platform (GCP)

> A cloud-native solution to ingest, analyze, and visualize retail sales data using GCP services like BigQuery, Cloud Functions, Vertex AI, and Looker Studio.

---

## 🚀 Overview

This project simulates a scalable data pipeline for a fictional retail chain to:
- Ingest raw transaction data via Cloud Storage
- Transform and load it into BigQuery for querying
- Visualize trends through dashboards
- Run customer churn predictions using Vertex AI

This replicates a **real-world data architecture**, similar to what a cloud consultant or solution architect would deploy for a retail client.

---

## 🛠️ Tech Stack (GCP Services Used)

| Service         | Purpose                                               |
|-----------------|--------------------------------------------------------|
| **Cloud Storage** | Store uploaded CSV data (sales, products, customers) |
| **Cloud Functions** | Trigger ETL when new data is uploaded              |
| **BigQuery**     | Store and analyze transformed retail data             |
| **Looker Studio** | Create real-time dashboards for analysis              |
| **Vertex AI**    | Build & deploy a churn prediction model               |

---

## 📊 Features

- ✅ Ingests CSV files from Cloud Storage into BigQuery
- ✅ Cleans and transforms sales + customer data
- ✅ Generates insights like:
  - Best-selling products
  - Region-wise revenue
  - Inventory forecasting
- ✅ Predicts customer churn using classification model (92% accuracy)
- ✅ Exposes results via Looker Studio dashboard

---

## 🧱 Architecture Diagram

