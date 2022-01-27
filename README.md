![alt text](https://media.wired.com/photos/5c9040ee4950d24718d6da99/191:100/w_2400,h_1256,c_limit/shoppingcart-1066110386.jpg)
# AWS Credit Card Transactions Stream and Batch Processing Data Pipeline

# Introduction & Goals
Cloud services have changed the way that businesses are operated. I have been working on data warehousing as a data engineer and are always exited to expand my toolbox of data engineering. With that in mind, I designed and built this data pipeline to build up knowledge in AWS and its components. The purpose of this project is to build a data pipeline to collect, transform, and store data into different data storages to meet the needs of data users. The credit card transactions dataset is sourced from Kaggle and will be fed into both stream and batch pipelines.

**Major Steps**
* Design an AWS data pipeline framework of stream and batch processing which is practical for real-world enterprises.
* Set up cloud components of stream and batch processing(API Gateway, Kinesis, Lambda Function, Dynamo DB, S3, Redshift and etc.)
* Troubleshoot and maintain the pipeline by using Cloudwatch

**Transactional Goals (Users)**
* To record customer/merchant info of each credit card transaction
* Fraud detection
* Access through: * credit card number and time 
                  * Access Merchant name

**Analytics Goals (Analysts)**
* Regional transaction analysis(e.g. customer purchase preference based on region )
* customer segmentation(e.g. Gender, age)

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set
The dataset [Credit Card Transactions Fraud Detection](https://www.kaggle.com/kartik2112/fraud-detection) is sourced from Kaggle. It is simulated with info of transactions, customers, merchants, and whether each transaction is a potential fraud. The reason why I choose this dataset is that it provides enough details for each major section. For example, transaction info includes date, time, credit card/transaction number and etc. Customer info includes location, job, dob, gender and etc. The dataset not only meets the needs of transactional purpose but also of analytical purpose. 

There are also concerns with the dataset although the advantages outweigh the disadvantages in my use case. One of the problems is that the dataset doesn't have customer and merchant IDs which is important for database normalization if the data needs to be stored in a relational database. In this case, I'll need to generate IDs for the customers and merchants.

# Used Tools
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/tool2.png)

## Client
The client is simulated by local PC with the data source downloaded from Kaggle in CSV format. The CSV file is read by python script and then the data is sent to AWS API endpoint through POST method.
## Connect
API Gateway is a very efficient API development tool which can run multiple versions of the same API simutaneously, allowing me to iterate, test and release new versions. I only need to pay for the the calls made. It's able to perform at any scale and the monitoring is also easy with Amazon Cloudwatch.
## Buffer
Kinesis is a great tool for me to stream process the credit card transactions data real-time with any amount of data, even if there are many different data sources. It's serverless so there's no need to manage the infrastructure by the developer.
## Processing
Lambda functions: In this project, the use cases of Lambda function are as follow.  
1. Lambda function processes the data from API Gateway and passes it to Kinesis.  
2. Lambda function processes the data from Kinesis and send it to different data stores(S3 & Dynamo DB in this project).  Kinesis Firehose: AWS Firehose checks on S3 manifest files that point to S3 data files, read the s3 data files and execute COPY Command to copy data into corresponding Redshift table. 

AWS Glue: Glue is the serverless ETL tool which provices great convinience. Crawlers automatically discover all the datasets, extract schema and store the information in a catalog for later querying and analysis. It also automatically generates the script for the ETL process so the developer doesn't need to start from scratch.
## Storage
Dynamo DB: Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. A partition kay(cc_num) and a sort key(trans_date_trans_time) are design to access data in this project.

S3: The data lake in this project. It'll be used to store both processed data as well as raw data.

Redshift: The OLAP database. Most of the analysis and visualization will be based on the data stored here. 
## Visualization

## Stream Processing
1. The layout of the stream processing
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/AWS%20Flow%20(3).png)
2. The work flow
* The local PC executes the Python script sending the credit card transactions data to API Gateway.
```
import requests
import pandas as pd

URL = 'the api gateway stage invoke url'

data = pd.read_csv('FraudTest.csv', sep = ',', index_col=False)
data_sample = data[:5]

for i in data_sample.index:
    try:
        export = data_sample.loc[i].to_json()

        response = requests.post(URL, data = export)

        print(response)
    except:
        print(data_sample.loc[i])
```
* API Gateway acts as a gate and a bridge between the local csv data and Kinesis data streams
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/APIGateway_Kinesis.jpg)
* The [Write-to-Kinesis](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/writeKinesis.py) Lambda function will be triggered once transaction data reaches the API Gateway and will pass the data received to Kinesis
* Kinesis Data Stream: A basic kinesis data stream has been created with the number of open shards = 1 and with the data retention period of one day. Once the event reaches kinesis, there are two Lambda functions will be triggered, [write-to-DynamoDB](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/write-kinesis-to-dynamodb.py) and [write-to-S3](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/write-kinesis-to-s3.py) respectively.
* [write-to-DynamoDB](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/write-kinesis-to-dynamodb.py) and [write-to-S3](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/write-kinesis-to-s3.py) will take the events received from Kinesis and load them into the OLTP table in DynamoDB and into S3 bucket respectively.
* Meanwhile, when data gets loaded into S3 bucket, Firehose delivery stream executes [COPY Command](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/CopyCommand.txt) to copy data from S3 bucket to Redshift following the structure of [jsonpath file](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/code/jsonpaths.json) stored in S3 bucket. Redshift will use S3 manifest files created by Firehose to look for the S3 data files that should be copied and then copy the corresponding data into Redshift table.
* With the steps above, the credit card transactions data will be successfully transformed and transported from the client to our data stores. 
## Batch Processing
1. The layout of the batch processing
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/Batch%20Processing%20Flow%20(1).png)
2. The work flow
* The Glue Crawler will be used to generate data catalogs for the data lives in S3 bucket and the target Redshift table.
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/Glue%20Catalog.png)(Glue Catalog)
* A Glue job will be created to transform the data based on the catalogs generated by Crawler and then load it to corresponding Redshift table. In this step, I will need to set up the data source and the data target for the job, and specify the processing framework. In this project, Spark is selected and a script will be generated automatically based on the job setup. The developer is also able to edit the script if changes are needed.
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/glue%20jub%20mapping.png)(Glue job mapping)
![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/blob/main/image/Glue%20Spark%20Script.png)(Glue Spark Script)
* Run the job created in the previous step and the ETL will be conducted. Processing info of status/error will be available in the Couldwatch log when job is done. 
## Visualizations

# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On
Linkedin: 

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
