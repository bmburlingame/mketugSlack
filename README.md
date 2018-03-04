# mketugSlack
A set of workers to post information in a slack channel

Clone this repo and run:
 
    ```$ pip install -r requirements.txt```

###Twitter Listener
Live listening to twitter to pull tweets from different users or contain certain hastags/keywords

To implement:
1. Get twitter API key (https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens)
2. Get Slack webhook URL for channel you want to post in (https://api.slack.com/apps).
3. Deploy heroku app (https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
4. To test locally, create a file '../.tug-env' or set as ENV variables in heroku
    ```
    ACCESS_TOKEN = <twitter-access-token>
    ACCESS_TOKEN_SECRET = <twitter-access-token-secret>
    CONSUMER_KEY = <twitter-consumer-key>
    CONSUMER_SECRET = <twitter-consumer-secret>
    WEBHOOK_URL = <slack-webhook-url>
    ```
5. For deployment to heroku, make sure you have a Profile in the top directory of the app containing
    ```
    worker: python twitter-slackbot-run.py
    ```
6. To change who/what you [listen for on twitter], edit the TWITTER.LISTENING variable in the [constants.py]

###Changes/updates coming
- Set up ability to store tweets in a postgres database
- Set up slash command to retrieve tweets from database
- More cool stuff


email me: burlingamebryan@gmail.com to contribute
03/04/2018 

[constants.py]: https://github.com/bmburlingame/mketugSlack/blob/master/constants.py
[listen for on twitter]: https://developer.twitter.com/en/docs/tweets/filter-realtime/overview