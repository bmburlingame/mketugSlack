import os

ENV_FILE = "../.tug-env"

class SetEnvironment:
    def __init__(self):
        try:
            from dotenv import load_dotenv
            load_dotenv(os.path.join(os.path.dirname(__file__), ENV_FILE))
            dotenv = os.environ
            os.environ.update(dotenv)
        except:
            dotenv = os.environ

SetEnvironment()

TUG_HASHTAG = 'mketug'

class TWITTER:
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

class SLACK:
    WEBHOOK_URL = os.environ['WEBHOOK_URL']