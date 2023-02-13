from app import app
from flask import jsonify
import requests
import time
from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult


def request_token() -> str:

    # Set body for post request.
    body = {
    'client_id': app.config['CLIENT_ID'],
    'client_secret': app.config['CLIENT_SECRET'],
    "grant_type": 'client_credentials'
    }

    # Make post request to Oauth2
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    # Checks if status_code is <400 and returns access token.
    if not r.ok:
        print(r.status_code, r.reason)
        raise Exception
    else:
        return r.json()['access_token']


def request_game(access_token: str, endpoint: str, filters: str) -> GameResult:

    wrapper = IGDBWrapper(app.config['CLIENT_ID'], access_token)

    byte_array = wrapper.api_request(
                f'{endpoint}.pb', # Note the '.pb' suffix at the endpoint
                filters
            )

    games_message = GameResult()

    games_message.ParseFromString(byte_array)
    
    time.sleep(1)

    return games_message