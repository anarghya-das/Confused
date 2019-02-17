import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
import tweepy

CONSUMER_KEY = 'baK58eDxGX0vybD2stNRcXtj5'
CONSUMER_SECRET = 'YNGfaQ5KF7utqSLfqltyKMEqOlPAzbypuZ4EthqTUwHy9Y88rO'
ACCESS_TOKEN = '541652003-Jqf6Pu4CA3zAlneX9Ws0Uq2d0egcB6lqAA8GDLjV'
ACCESS_TOKEN_SECRET = '3z34oOvw1be7hppYEcMGR2cSxYHgRiijk2h6VZAOV0Bgp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status("Tweet here")