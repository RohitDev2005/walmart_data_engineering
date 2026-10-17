# Walmart End-to-End Data Engineering Pipeline

An end-to-end data engineering project that transforms raw Walmart retail data into structured, analytics-ready datasets using Python, PostgreSQL, Databricks, dbt, and Apache Airflow.

## 📌 Overview

Retail data is generated across multiple business entities, including customers, products, stores, employees, and orders. Before this data can support reliable analysis, it must be ingested, organized, transformed, and validated through a consistent data pipeline. 

This project demonstrates a modular data engineering workflow for Walmart retail data, combining PostgreSQL-based ingestion, Databricks processing, dbt transformations, and Apache Airflow orchestration.

## 🎯 Problem Statement

Raw retail data is not immediately suitable for analytical use. Data engineers need a structured process to ingest source data, organize transformations, validate data quality, and coordinate dependent tasks. The goal of this project is to build a maintainable pipeline that separates raw data ingestion from downstream transformations and produces structured datasets for analytical workloads.

## 💡 Solution

The project combines two primary components:
*   **Data Ingestion and Database Exploration:** Uses Python and Neon PostgreSQL to load Walmart CSV datasets into structured raw tables, with Neon MCP supporting AI-assisted database interaction.
*   **Data Transformation and Orchestration:** Uses Databricks for incremental data ingestion and Apache Airflow to coordinate the workflow, while dbt manages SQL transformations, snapshots, freshness checks, and data quality tests.

## 🏗️ Architecture

```text
Walmart CSV Datasets
        │
        ▼
Python Data Ingestion
        │
        ▼
Neon PostgreSQL (Raw Schema)
        │
        ▼
Apache Airflow (Workflow Orchestration)
        │
        ▼
  Databricks Job
        │
        ▼
 dbt Transformations
        │
        ├─► Silver Technical Models
        ├─► Silver Business Models
        └─► Gold Models
        │
        ▼
Analytics-Ready Data
```

*Note: The ingestion and orchestration components are maintained separately in the repository. The diagram illustrates the overall workflow they are designed to support.*

## ⚙️ Data Processing and Transformation

The pipeline works with six core Walmart datasets:
*   Customers
*   Employees
*   Orders
*   Order Items
*   Products
*   Stores

The dbt transformation layer organizes data processing into the following stages:

*   **Silver Technical Layer:** Creates entity-level technical models from source data.
*   **Silver Business Layer:** Combines and organizes data into business-oriented models, including an order-related one-big-table (OBT) model.
*   **Gold Layer:** Contains ephemeral models and an order fact model designed for downstream analytical use.
*   **Data Validation and History:** Includes dbt tests, source freshness checks, and snapshots for selected business entities to support data quality and change tracking.

## 🚀 Engineering Highlights

*   **Ingestion:** Python-based CSV ingestion into cloud-hosted PostgreSQL using Neon.
*   **AI Exploration:** AI-assisted database exploration through Neon MCP.
*   **Processing:** Incremental data ingestion through managed Databricks jobs.
*   **Orchestration:** Workflow orchestration and task dependencies managed using Apache Airflow.
*   **Data Modeling:** Advanced SQL transformations and layered data modeling built via dbt.
*   **Quality Assurance:** Built-in data quality checks, source freshness validation, and dbt snapshots for change data capture (CDC).
*   **Environment:** Docker Compose setup for spinning up the local Airflow environment.
*   **DevOps:** Version control powered by Git and GitHub.

## 🛠️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Programming & Querying** | Python, SQL |
| **Database** | PostgreSQL, Neon |
| **Database Interaction** | Neon MCP |
| **Data Processing** | Databricks |
| **Transformation** | dbt |
| **Orchestration** | Apache Airflow |
| **Environment** | Docker Compose |
| **Version Control** | Git, GitHub |

## 🏆 Project Outcome

This project brings together core data engineering practices into a single portfolio architecture: structured ingestion, layered SQL transformations, robust workflow orchestration, comprehensive data quality validation, and historical change tracking. It successfully demonstrates how raw, disconnected retail datasets can be organized into a repeatable processing workflow ready for production-level analytical use.

## 🌟 About Me

Hi! I’m a Computer Engineering student with a strong interest in **Data Analytics and Data Engineering**.  
I enjoy working with SQL, data modeling, and building end-to-end data pipelines.  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/rohit-devshatwar-178249296)  
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge\&logo=leetcode\&logoColor=black)](https://leetcode.com/u/Rohit_Devshatwar/)  
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge\&logo=geeksforgeeks\&logoColor=white)](https://www.geeksforgeeks.org/profile/devshatwxqs5)
