import requests
from dotenv import dotenv_values
from igdb.wrapper import IGDBWrapper

config = dotenv_values('.flaskenv')

client_id = config['CLIENT_ID']
client_secret = config['SECRET']
streamer_name = 'Fextralife'

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}

r = requests.post('https://id.twitch.tv/oauth2/token', body)

#data output
keys = r.json();

print(keys)

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

print(headers)

wrapper = IGDBWrapper(config['CLIENT_ID'], keys['access_token'])

byte_array = wrapper.api_request(
            'covers.pb', # Note the '.pb' suffix at the endpoint
            'fields *; where id = (120815); limit 50;'
)

# Protobuf API request
from igdb.igdbapi_pb2 import GameResult, CoverResult
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields name,cover.url,genres.name; where id = (123); limit 50;'
          )
# print(byte_array)
games_message = GameResult()
games_message.ParseFromString(byte_array)
print(games_message.games[0].n)