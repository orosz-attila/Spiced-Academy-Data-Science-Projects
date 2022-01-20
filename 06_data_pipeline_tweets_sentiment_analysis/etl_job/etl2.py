import time
import pymongo
from sqlalchemy import create_engine
import psycopg2
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

time.sleep(10)

mongo_connection = pymongo.MongoClient(host="mongodb", port=27017) # Establish a connection to the MongoDB server
twitter_db = mongo_connection.twitter # Select the twitter database of the MongoDB

postgres_connection = create_engine('postgresql://postgres:****@postgresdb:5432/postgres', echo=True) # Establish a connection to Postgres

# Creating table in postgres named postgres_tweets
postgres_connection.execute('''
    CREATE TABLE IF NOT EXISTS postgres_tweets (
        timestamp VARCHAR(500),
        text VARCHAR(500),
        score VARCHAR(500)
);
''')

def extract():
    ''' Extracts tweet dictionary from mongodb twitter database, tweets table'''
    extracted_tweets = list(twitter_db.tweets.find(limit = 5))
    return extracted_tweets


def transform(extracted_tweets):
    ''' Transforms data: gets score of sentiment analysis from text. '''
    s_analyzer  = SentimentIntensityAnalyzer()

    transformed_tweets = []

    for tweet in extracted_tweets:
        sentiment = s_analyzer.polarity_scores(tweet['text'])  
        tweet['sentiment'] = sentiment['compound']
        transformed_tweets.append(tweet)
    return transformed_tweets


def load(transformed_tweets):
    for tweet in transformed_tweets:
        query = "SELECT timestamp FROM postgres_tweets"
        loaded_tweets = list(postgres_connection.execute(query))
        #logging.critical('loaded tweets {}'.format(transformed_tweets))
        #logging.critical('timestamps {}'.format(loaded_tweets))
        if tweet['created_at'] not in loaded_tweets:
            insert_query = "INSERT INTO postgres_tweets VALUES (%s, %s, %s);"
            postgres_connection.execute(insert_query,(tweet['created_at'], tweet['text'], tweet['sentiment']))
        logging.critical('---Inserted a new tweet into postgres---')
    

if __name__== "__main__":
### example: run ETL job every 2 minutes
    while True:
        extracted_tweets = extract()
        transformed_tweets = transform(extracted_tweets)
        load(transformed_tweets)
        time.sleep(120) 