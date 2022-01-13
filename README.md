![alt text](https://media.wired.com/photos/5c9040ee4950d24718d6da99/191:100/w_2400,h_1256,c_limit/shoppingcart-1066110386.jpg)
# AWS Credit Card Transactions Stream and Batch Processing Data Pipeline

# Introduction & Goals
Cloud services have changed the way that businesses are operated. I have been working on data warehousing and are always exited to expand my toolbox of data engineering. With that in mind, I designed and built this data pipeline to build up knowledge in AWS and its components. The purpose of this project is to build a complete data pipeline to collect, transform, and store data into different data storages to meet the needs of data users. The credit card transactions dataset is sourced from Kaggle and will be fed into both stream and batch pipelines.

**Major Steps**
* Design AWS data pipeline framework of data streaming and batch processing that is used by enterprises.
* Set up cloud components of data streaming and batch processing(API Gateway, Kinesis, Lambda Function, Dynamo DB, S3, Redshift and RDS etc.)
* Troubleshoot and maintain the pipeline by using Cloudwatch

**Transactional Goals (Users)**
To record customer/merchant info of each credit card transaction
Fraud detection
Access through: * credit card number and time 
                * Access Merchant name

**Analytics Goals (Analysts)**
Regional transaction analysis(e.g. customer purchase preference based on region )
customer segmentation(e.g. Gender, age)

- Orient this section on the Table of contents
- Write this like an executive summary
  - With what data are you working
The transaction data is simulated and is comprehensive with transaction details(ID, date, time and etc.), customer & merchant info and fraud alert.
  - What tools are you using
The project is based on AWS with tools not limited to API Gateway, Lambda, Kinesis, Dynamo DB, S3, and Redshift.
  - What are you doing with these tools
  - Once you are finished add the conclusion here as well

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
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set
- Explain the data set
The dataset [Credit Card Transactions Fraud Detection Dataset](https://www.kaggle.com/kartik2112/fraud-detection) is sourced from Kaggle. It is simulated with details that include transaction, customer, merchant, and whether each transaction is fraud. The reason why I chose this dataset is that is provides enough details for each major section. For example, transactions includes date, time, credit card/transaction number and etc. Customer info includes Location, job, dob, gender and etc regarding. The dataset meets the needs not only for transactional goals but also for analytical goals. 

There are also problems with the dataset although the advantages outweigh the disadvantages in our use case. One of the problems is that the dataset doesn't have customer and merchant IDs which is important for database normalization if the data needs to be stored in a relational database. In this case, we'll need to generate IDs for the customers and merchants.

# Used Tools
- Explain which tools do you use and why
- How do they work (don't go too deep into details, but add links)
- Why did you choose them
- How did you set them up

## Connect
## Buffer
## Processing
## Storage
## Visualization

# Pipelines
- Explain the pipelines for processing that you are building
- Go through your development and add your source code

## Stream Processing
### Storing Data Stream
### Processing Data Stream
## Batch Processing
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
Add the link to your LinkedIn Profile

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
