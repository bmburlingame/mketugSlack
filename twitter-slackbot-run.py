from twitterListener.twitter_slack import TwitterListener
from constants import *
from tweepy import OAuthHandler
from tweepy import Stream

auth = OAuthHandler(TWITTER.CONSUMER_KEY, TWITTER.CONSUMER_SECRET)
auth.set_access_token(TWITTER.ACCESS_TOKEN, TWITTER.ACCESS_TOKEN_SECRET)

twitterStream = Stream(auth, TwitterListener())
twitterStream.filter(track=TWITTER.LISTENING, follow=TWITTER.USER_IDS)