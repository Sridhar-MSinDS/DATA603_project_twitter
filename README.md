# DATA603_project_twitter

# Why do we need to do twitter data streaming?

Twitter data streaming is a valuable source of real-time information that can be analyzed across different industries for various purposes. Here are some key reasons why analyzing Twitter data streams is beneficial: 
1. Real-Time Sentiment Analysis
2. Trend Detection
3. Crisis Management and Response
4. Predictive Analytics
5. Political Analysis and Social Research
6. Health Monitoring

# Which big data tools or frame works that are available in the market to handle big data?

When it comes to processing Twitter streaming data, especially within the context of big data, there are several powerful frameworks and tools designed to handle big data processing, and analysis.
1. Apache Kafka
2. Apache Storm
3. Apache Spark
4. Apache Flink
5. Apache NiFi

# Why we choosen Apache Spark over other tools for streaming?

Choosing Apache Spark over other tools for streaming due to the numerous benefits, especially in contexts where you need robust data processing capabilities.
Some of the advantages are:
1. It can process both historical (batch) and real-time (streaming) data.
2. Spark provides high-level APIs in Python, Java, Scala, and R.
3. Spark includes libraries for SQL queries, machine learning (MLlib), graph processing (GraphX), and even deep learning integration (via projects like BigDL). 
4. Spark achieves high performance for both streaming and batch processing through its advanced DAG (Directed Acyclic Graph) execution engine which optimizes workflows dynamically.
5. Through Resilient Distributed Datasets (RDDs), Spark provides inherent fault tolerance in the data.
6. Spark integrates easily with other big data tools like Hadoop for storage, Kafka for message queuing, and various NoSQL databases for data output. 

# How twitter streming is done using apache spark?

We need to setup a Developer API acocunt with Twitter and create an application to get credentials. 
Step 1: Environment Setup
(Install apache spark, python, tweepy in python library)

Step 2: Obtain Twitter API Credentials
Consumer Key
Consumer Secret
Access Token
Access Token Secret

Step 3: Setup Tweepy for Streaming Twitter Data
Tweepy to set up a stream listener that collects the tweets and sends them to Spark.

Step 4: Integrate with Spark Streaming
One common method is to use a socket connection, where Tweepy pushes tweets to a local port that Spark Streaming is listening to.

Step 5: Sending Data from Tweepy to Spark
Modify the Tweepy on_status method to send data to the port where Spark is listening.
