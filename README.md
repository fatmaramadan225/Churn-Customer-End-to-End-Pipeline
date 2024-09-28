# Churn-Customer-End-to-End-Pipeline
This project is a comprehensive data engineering solution developed as part of the ITI Data Engineering Track graduation project. It demonstrates real-time data ingestion, processing, storage, and live analytics using a multi-cloud architecture. The project utilizes a combination of Apache Kafka, Apache Airflow, PySpark, Hadoop, Hive, SQL Server, Azure SQL Database, Docker, and Power BI.

![pipeline](https://github.com/user-attachments/assets/b33648ff-a1b9-4f82-ac7b-bedd402083bb)

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Technologies Used](#technologies-used)
- [Pipeline Workflow](#pipeline-workflow)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [Contributors](#contributors)
- [Demo](#demo)

## Architecture Overview
The project consists of a scalable, real-time data pipeline that ingests, processes, and stores data using different services and technologies across multiple cloud platforms.

### Key Components:
1. **Data Ingestion**: Streaming data using Apache Kafka.
2. **Data Orchestration**: Managed by Apache Airflow running on AWS EC2.
3. **Data Processing (PySpark)**:
    - First branch writes raw streaming data to Azure SQL Database for backup.
    - Second branch runs a machine learning classification model and stores the results in SQL Server.
    - Third branch writes data to Hadoop and processes it with Hive SQL for big data solutions.
4. **Data Visualization**: Processed data is displayed on Power BI for live analytics and reporting.
5. **Multi-cloud Deployment**: Services run across AWS EC2 and Azure (Azure SQL Database).

## Technologies Used

- **Kafka**: Used for real-time data streaming.
- **Airflow**: Workflow orchestration and scheduling.
- **PySpark**: Data processing and machine learning.
- **Azure SQL Database**: Stores raw data for backup.
- **SQL Server**: Stores processed data and results of ML classification.
- **Hadoop**: Distributed data storage for big data processing.
- **Hive**: Query engine for large datasets stored in Hadoop.
- **Power BI**: Real-time dashboards for visualizing processed data.
- **Docker**: Containerization of services for portability.
- **AWS EC2**: Hosting for Kafka, Airflow, PySpark, and Hadoop services.

## Pipeline Workflow

### 1. **Data Ingestion**
- Apache Kafka simulates data streaming, allowing continuous data ingestion.
- Apache Airflow orchestrates the data ingestion process, scheduling tasks and managing dependencies.

### 2. **Data Processing with PySpark (Three Branches)**
- **Branch 1 (Backup)**: Consumes the data stream from Kafka and writes raw data to **Azure SQL Database** for backup.
- **Branch 2 (ML Model & ODS)**:
  - Runs a **PySpark ML** classification model.
  - Stores the results in **SQL Server** as:
    1. **Operational Data Store (ODS)**: A table that records all operations and results in real-time.
    2. **Distinct Data Table**: A table that stores distinct values after filtering, used for live analytics.
- **Branch 3 (Big Data Storage)**: Writes streaming data to **Hadoop** and uses **Hive SQL** for querying the big data.

### 3. **Visualization with Power BI**
- The cleaned and distinct data is connected to **Power BI** for real-time visualization and dashboard creation.

## Setup and Installation

### Prerequisites

- **AWS EC2**: Set up an EC2 instance to run Kafka, Airflow, PySpark, and Hadoop services.
- **Azure SQL Database**: Create a database in Azure to store raw data.
- **SQL Server**: Ensure SQL Server is accessible for storing processed ML data.
- **Docker**: Install Docker for containerized service management.
- **Power BI**: Set up Power BI for visualizing the data.

## Usage
- Start Kafka: Ensure Kafka is streaming data.
- Trigger Airflow DAGs: Use Airflow to manage and trigger the PySpark jobs.
- Monitor PySpark Jobs: PySpark will process the data in the three branches, saving raw data in Azure SQL Database, ML results in SQL Server, and streaming data in Hadoop.
- Visualize Data in Power BI: Open Power BI and ensure real-time data is visualized from SQL Server.

## Dockerization

The following services have been Dockerized for ease of deployment and scaling:
- **Kafka** and **Airflow** are **Dockerized on EC2**.
    - They serve as shared resources for managing data streaming (Kafka) and workflow orchestration (Airflow) in the pipeline.
- **PySpark**, **Hadoop**, and **Hive** are Dockerized locally.
- Networking between local containers and EC2-based services is essential for proper pipeline functioning.

To start the Dockerized services locally (PySpark, Hadoop, Hive):
```bash
docker-compose up -d
```

## Contributors

- [Mahmoud Hassanen](https://github.com/MahmoudHassanen99)
- [Fatma Ramadan](https://github.com/fatmaramadan225) 
- [Tasneem Samy](https://github.com/neema233) 
- [Ahmed Zahran](https://github.com/Zahran22) 
- [Yara Mamdouh]()

## Demo

- **Demo Video**: [Watch the demo](https://drive.google.com/file/d/1Q3ETz0VFPQ0xynl6nblZ4W4Nn9WsOrKW/view?usp=drive_link)


