# Customer_Churn-ITI_Graduation-
## Customer_Churn
Customer churn refers to the phenomenon where customers stop using a company's products or services over a specific period. 
It is a critical metric for businesses as it directly impacts revenue, customer growth, and market share. 
Churn can occur for various reasons, such as dissatisfaction with the product, better offers from competitors, or changes in customer needs.

## Pipline

![Pipline-final (1)](https://github.com/user-attachments/assets/b858a4d5-673b-46be-89ff-def423e62dc1)


## Tools
1-Kafka\
2-Airflow\
3-azure sql db\
4-Pyspark\
5-SQL Server\
6-Power BI\
7-Hadoop\
8-Hive
## Dataset
***CustomerID (int):*** Unique identifier for each customer.\
***Age (int):*** Age of the customer.\
***Gender (object):*** Gender of the customer.\
***Tenure (int):*** Duration of the customer's relationship with the company in months.\
***Usage Frequency (int):*** Frequency of service usage.\
***Support Calls (int):*** Number of support calls made by the customer.\
***Payment Delay (int):*** Number of days payment was delayed.\
***Subscription Type (object):*** Type of subscription (e.g., Basic, Standard, Premium).\
***Contract Length (object):*** Length of the subscription contract (e.g., Monthly, Annual).\
***Total Spend (int):*** Total amount spent by the customer.\
***Last Interaction (int):*** Number of days since the last interaction.


![Screenshot 2024-09-25 123859](https://github.com/user-attachments/assets/46a74ba7-9a6d-4cc8-8b40-798f25da1dbb)

## Data Extraction

#### kafka producer
. each one second gnerate onre record in kafka topic "Customer_Churn"
#### kafka consumer (pyspark)
. read data from kafka topic then apply preprocessing and ML model

## Workflow Orchestration
. with Apache Airflow Airflow as Orchestrator: Airflow is used to manage and orchestrate the entire process

## Preprocessing
After receeving data from kafka topic, it is in json format so we need some preprocessing on it
Handling columns data types\
. Dealing with nulls (Numerical & Categorical)\
. Schema\
. Define Schema to be fitted with orginal schema which model trained on
. Small files issue\
. Define a trigger for pyspark streaming writer in hadoop\
. Colease for pyspark stream ingwriter in hadoop

## Azure SQL
#### Why Azure SQL DB on Cloud?
. Scalability and Elasticity:\
. Ease of Data Access for Further Processing\
. Fully Managed PaaS\
. Compliance and Security\
. Easy to Use

#### Azure SQL DB For our Approach
. Backup of Raw Data Before Labeling\
. Easily Recap Raw Data\
. Public Access for Read/Write from Multiple Locations

## Pyspark ml Model
. Churn Prediction Model Overview
#### Objective:
. Predict customer churn (1 = Churned, 0 = Not Churned).
#### Technology:
. Implemented using PySpark ML, enabling scalable and efficient machine learning.
#### Streaming Approach:
. Analyzes customer data in real-time for immediate predictions.
#### Distributed Computing:
. Handles large datasets efficiently, processing thousands of records simultaneously.
#### Business Impact:
. Empowers proactive strategies to reduce churn and improve customer retention.

#### Explain each stage of the pipeline:
. Indexers: Convert categorical variables into numerical indices.
. Assembler: Combine features into a single feature vector.
. Logistic Regression (LR): The classification algorithm used.

#### Model Training:
. Trained on Google Colab and saved on Google Drive
. Interpreting the Confusion Matrix The confusion matrix can be interpreted as follows:\
   . True Negatives (TN): 49,384 - The number of customers who did not churn and were correctly predicted as not churned.\
   . False Positives (FP): 7,678 - The number of customers who did not churn but were incorrectly predicted as churned.\
   . False Negatives (FN): 9,620 - The number of customers who did churn but were incorrectly predicted as not churned.True Positives (TP): 65,513
     The number of customers who churned and were correctly predicted as churned.\


#### Having Challenge
1- Large Amount of Historical Data.\
2- Very Fast Incremental Data

#### Solution
. In Spark Streaming, triggers control how often your streaming job processes incoming data. By default, Spark Streaming uses micro-batch processing, where it divides the incoming data 
  into small batches and processes them at a specified interval.\
. Batching Small Files.\
. Combining Data.\
. Dynamic File Sizing.\
. Compression.

#### 2- coalesce
. Coalescing is a transformation that reduces the number of partitions in a Spark DataFrame or RDD without performing a full shuffle of the data. It can merge partitions, effectively combining smaller datasets into larger ones.

. How Coalescing Helps with Small Files in HDFS?\
. Reducing the Number of Output Files\
. Minimizing Write Overhead.\
. Improving Read Performance.


## Future Plans
. Fully Cloud-Based Automation\
. Enhanced Model Performance\
. Multi-Cloud Integration


