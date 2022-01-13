![alt text](https://github.com/DefoeZhang/data-engineering-aws-credit-card-transactions/Cart.jpg?raw=true)
# AWS Stream and Batch Processing Data Pipeline for Credit Card Transactions

# Introduction & Goals
As a data engineering professional with more than 2 years of experience, I have been working on data warehousing and are exited to expand my toolbox of data engineering. With that in mind, I built this AWS data pipeline. The purpose of this project is to build up a complete data pipeline to collect, transform, and store data into data storages to meet the needs of data users. The credit card transactions dataset is sourced from Kaggle and will be fed into both stream and batch pipelines.

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
- Why did you choose it?
- What do you like about it?
- What is problematic?
- What do you want to do with it?

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
