import tweepy
from constants import *

consumer_key = TWITTER.CONSUMER_KEY
consumer_secret = TWITTER.CONSUMER_SECRET
access_token = TWITTER.ACCESS_TOKEN
access_token_secret = TWITTER.ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.get_user(screen_name = 'tableau')

print user.id
