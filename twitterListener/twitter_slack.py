# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener

import json
import requests
import time
import calendar
from constants import *

# This is a basic listener that just prints received tweets to stdout.
class TwitterListener(StreamListener):

    def slack_color(self, twitter_handle, hashtags):
        """Get the color for the slack channel"""

        # If tweet is from tableau
        if twitter_handle == 'tableau':
            return '#30A3C0'

        # If tweet contains #mketug
        hashtags = [x['text'].lower() for x in hashtags]
        if TUG_HASHTAG in hashtags:
            return '#23E12B'

        # If not authored by tableau or a hashtag for mketug, return black
        return '#101E10'

    def parse_tweet(self, df):
        """Parse the tweet to obtain information for slack post"""

        # Original twitter post information
        original_twitter_handle = df['user']['screen_name']
        original_twitter_photo = df['user']['profile_image_url']
        id_str = df['id_str']
        original_tweet_url = 'https://twitter.com/' + original_twitter_handle + '/status/' + id_str
        hashtags = df['entities']['hashtags']

        # Get text of tweet
        try:
            tweet_text = df['extended_tweet']['full_text'] # If tweet is longer than 140 chars
        except:
            tweet_text = df['text']

        # If tweet is a reply then build tweet url for original tweet
        try:
            in_reply_to_screen_name = df['in_reply_to_screen_name']
            in_reply_to_status_id = df['in_reply_to_status_id_str']
            replying_to_url = 'https://twitter.com/' + in_reply_to_screen_name + '/status/' + in_reply_to_status_id
            replying_payload = {
                "title": "Replying to: " + replying_to_url,
                "short": False
            }
        except:
            replying_payload = {}

        # Get color for slack channel
        color = self.slack_color(original_twitter_handle, hashtags)

        # Compile message for slack
        slack_data = {"attachments": [
                {
                    "fallback": "New tweet from @" + original_twitter_handle,
                    "color": color,
                    "author_name": "By: @" + original_twitter_handle,
                    "author_link": "https://twitter.com/" + original_twitter_handle,
                    "author_icon": original_twitter_photo,
                    "title": "Tweet Link",
                    "title_link": original_tweet_url,
                    "text": tweet_text,
                    "fields": [replying_payload],
                    "footer": TUG_HASHTAG.upper() + " Twitter API",
                    "footer_icon": SLACK.FOOTER_IMAGE_URL,
                    "ts": calendar.timegm(time.gmtime())
                }]
        }
        return slack_data

    def post_in_slack(self, payload):
        """Post tweet in slack channel"""
        requests.post(SLACK.WEBHOOK_URL,
                      data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'}
                      )

    def on_data(self, tweet_data):
        """Wait for tweet then parse"""
        data = json.loads(tweet_data)

        # Ignore tweets not in english and ignore retweets
        if data['lang'] != 'en' or 'RT @' in data['text']:
            return True

        try:
            # Clean and parse data and format slack message
            slack_message = self.parse_tweet(data)

            # Post in slack channel
            self.post_in_slack(slack_message)
        except:
            pass

        return True

    def on_error(self, status):
        print status
