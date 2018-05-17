from constants import *
from flask import Flask, request, jsonify, abort
app = Flask(__name__)

@app.route("/storypoints", methods=['POST'])

def StoryPoints():

    data = {'thing': 'Hello', 'other_thing': 'World!'}

    token = request.form.get('token', SLACK.SLACK_API_TOKEN)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)

    # Validate the request parameters
    if not token:  # or some other failure condition
        abort(400)


    return jsonify({
        # Uncomment the line below for the response to be visible to everyone
        # 'response_type': 'in_channel',
        'text': 'More fleshed out response to the slash command',
        'attachments': [
            {
                'fallback': 'Required plain-text summary of the attachment.',
                'color': '#36a64f',
                'pretext': 'Optional text above the attachment block',
                'author_name': 'Bobby Tables',
                'author_link': 'http://flickr.com/bobby/',
                'author_icon': 'http://flickr.com/icons/bobby.jpg',
                'title': 'Slack API Documentation',
                'title_link': 'https://api.slack.com/',
                'text': 'Optional text that appears within the attachment',
                'fields': [
                    {
                        'title': 'Priority',
                        'value': 'High',
                        'short': False
                    }
                ],
                'image_url': 'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&h=350',
                'thumb_url': 'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&h=350'
            }
        ]
    })
