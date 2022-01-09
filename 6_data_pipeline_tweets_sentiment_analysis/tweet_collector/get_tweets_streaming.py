import tweepy
import credentials
import pymongo
import time

mongo_connection = pymongo.MongoClient(host="mongodb", port=27017)
twitter_db = mongo_connection.twitter

def get_auth_handler():
    """
    Function for handling Twitter Authentication. See course material for 
    instructions on getting your own Twitter credentials.
    """
    auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    return auth


class MaxTweetsListener(tweepy.StreamListener):

    def __init__(self, max_tweets, *args, **kwargs):
        # initialize the StreamListener
        super().__init__(*args, **kwargs)
        # set the instance attributes
        self.max_tweets = max_tweets
        self.counter = 0

    def on_connect(self):
        print('connected. listening for incoming tweets')

    def on_status(self, status):
        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""

        # increase the counter
        self.counter += 1

        tweet = {
            'text': status.text,
            'created_at': status.created_at
        }
        
        print(f'New tweet arrived: {tweet["text"]}')
        
        twitter_db.tweets.insert_one(tweet) # creating the tweets table 
        
        # check if we have enough tweets collected
        if self.max_tweets == self.counter:
            # reset the counter
            self.counter = 0
            # return False to stop the listener
            return False

    def on_error(self, status):
        if status == 420:
            print(f'Rate limit applies. Stop the stream.')
            return False


if __name__ == '__main__':
    auth = get_auth_handler()
    listener = MaxTweetsListener(max_tweets=5)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Berlin'], languages=['en'], is_async=False)