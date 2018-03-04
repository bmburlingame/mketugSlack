import os

ENV_FILE = "../.tug-env"
TUG_HASHTAG = 'mketug'

class SetEnvironment:
    def __init__(self):
        try:
            # For local testing
            from dotenv import load_dotenv
            load_dotenv(os.path.join(os.path.dirname(__file__), ENV_FILE))
            dotenv = os.environ
            os.environ.update(dotenv)
        except:
            # For heroku
            dotenv = os.environ

SetEnvironment()

class TWITTER:
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

    LISTENING = [TUG_HASHTAG, 'from:tableau']

class SLACK:
    WEBHOOK_URL = os.environ['WEBHOOK_URL']