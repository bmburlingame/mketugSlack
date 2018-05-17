import os

ENV_FILE = "../.tug-env"
TUG_HASHTAG = 'mketug'
TABLEAU_USERID = '14792516'

class SetEnvironment:
    def __init__(self):
        """Set variables from ENV file to environment or pull variables from Heroku"""
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

    # Edit this to change who you listen to
    LISTENING = [TUG_HASHTAG]
    USER_IDS = [TABLEAU_USERID]

class SLACK:
    WEBHOOK_URL = os.environ['WEBHOOK_URL']
    FOOTER_IMAGE_URL = "https://yt3.ggpht.com/a-/AJLlDp3qx91Z4QkUvGvBPJAB4aCTFdtU7ZPG_WidFA=s900-mo-c-c0xffffffff-rj-k-no"
    SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']
    SLACK_TEAM_ID = os.environ['SLACK_TEAM_ID']
