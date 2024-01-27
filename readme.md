Welcome

After git clone;

1) Set up environmet
2) Set up .env file for API creds
3) Change Bootstrap servers from producer.py file

python3.8 -m venv producerenv

source producerenv/bin/activate

pip install -r requirements-producer.txt

touch .env

newsapi='CREATE_API_KEY_FROM_NEWS_API'

https://newsapi.org/