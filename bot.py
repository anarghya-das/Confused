import tweepy
import time
import tweepy

CONSUMER_KEY = 'CONSUMER KEY'
CONSUMER_SECRET = 'SECRET CONSUMER KEY'
ACCESS_TOKEN = 'ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'SECRET ACCESS TOKEN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet(twt):
    api.update_status(twt)