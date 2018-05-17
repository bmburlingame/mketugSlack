from constants import *
from flask import Flask, request, jsonify, abort
app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form['token'] == SLACK.SLACK_API_TOKEN
    is_team_id_valid = request.form['team_id'] == SLACK.SLACK_TEAM_ID

    return is_token_valid and is_team_id_valid


@app.route('/storypoints', methods=['POST'])
def storypoints():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='HI',
    )