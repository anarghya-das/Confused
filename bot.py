import tweepy
import time
import tweepy

CONSUMER_KEY = '5'
CONSUMER_SECRET = 'O'
ACCESS_TOKEN = 'V'
ACCESS_TOKEN_SECRET = 'p'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status("Tweet here")
