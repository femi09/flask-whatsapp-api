from flask import Flask, request
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

verify_token = os.getenv('VERIFY_TOKEN')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/webhook")
def webhook_whatsapp():
    """__summary__: Get message from the webhook"""
    hub_token = request.args.get('hub.verify_token')

    hub_challenge = request.args.get('hub.challenge')

    hub_mode = request.args.get('hub.mode')

    if hub_token == verify_token and hub_mode == "subscribe":
        return hub_challenge

    return "Authentication failed. Invalid Token."


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.run()
