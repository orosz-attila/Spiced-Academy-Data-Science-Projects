import time
import requests
from sqlalchemy import create_engine
import psycopg2
import logging

time.sleep(10)

# Establish a connection to Postgres

postgres_connection = create_engine('postgresql://postgres:*********@postgresdb:5432/postgres', echo=True)

webhook_url = "https://hooks.slack.com/services/*********"

def getting_tweets_from_postgres():
    slacked_tweets = []
    last_tweets = list(postgres_connection.execute("SELECT * FROM postgres_tweets ORDER BY timestamp DESC LIMIT 5"))
    for tweet in last_tweets:
        if tweet in slacked_tweets:
            continue    
        else: 
            slacked_tweets.append(tweet)
    logging.critical(slacked_tweets)
    return(slacked_tweets)


def posting_in_slack(slacked_tweets):
    for tweet in slacked_tweets:
        # stringified_tweet = str(tweet)
        data = {'text': tweet[0]}
        requests.post(url=webhook_url, json=data)


if __name__== "__main__":
    slacked_tweets = getting_tweets_from_postgres() 
    posting_in_slack(slacked_tweets)
