from constants import *
from flask import Flask, request, jsonify, abort
app = Flask(__name__)

@app.route("/storypoints")

def StoryPoints():

    data = {'thing': 'Hello', 'other_thing': 'World!'}

    token = request.form.get('token', SLACK.SLACK_API_TOKEN)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)

    # Validate the request parameters
    if not token:  # or some other failure condition
        abort(400)


    return "Well hey there!!!!"
