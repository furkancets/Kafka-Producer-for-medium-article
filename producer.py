from datetime import datetime, timedelta
import requests
from kafka import KafkaProducer
import time
import json
from dotenv import load_dotenv
import os

load_dotenv()
# Kafka bootstrap server configuration
######PLEASE CHANGE YOUR BOOTSTRAP SERVERS HOST IP'S#########
bootstrap_servers = '192.168.67.7:9092,192.168.67.5:9092,192.168.67.6:9092'
topic_name = 'newsapiproducerv1'

# Kafka producer configuration
producer = KafkaProducer(
       bootstrap_servers=bootstrap_servers,
       value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

today = datetime.now()

two_days_ago = today - timedelta(days=2)

day_to_use = two_days_ago.strftime("%Y-%m-%d")

# News API URL
news_api_url = (f'https://newsapi.org/v2/everything?'
                f'q=Apple&'
                f'from={day_to_use}&'
                f'to={day_to_use}&'
                f'language=en&'
                f'apiKey={os.getenv("newsapi")}')

# Fetch news articles from the News API
response = requests.get(news_api_url)
data = response.json()

# Check if the request was successful
if response.status_code == 200 and data.get('status') == 'ok':
       # Extract articles
       articles = data.get('articles', [])
       
       current_time = datetime.now().strftime("%Y%m%d%H%M%S")

       # Publish each article to the Kafka topic
       for index, article in enumerate(articles):
              # Convert the article to a string for serialization
              
              
              time.sleep(1)

              producer.send(topic_name, value=article)
              
              print(f"Published article to Kafka: {article}")

       # Flush and close the Kafka producer
       producer.flush()
       producer.close()

else:
       print(f"Error fetching news data. Status code: {response.status_code}, Message: {data.get('message')}")
