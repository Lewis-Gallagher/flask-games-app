from app import app
from flask import render_template
from app.request import request_token, request_game

@app.route('/')
@app.route('/index')
def index():

    access_token = request_token()

    req = request_game(access_token=access_token,
                       endpoint='games',
                       filters='fields name,rating,cover.url; sort rating_count desc; where rating <= 100 & rating > 0;')

    for game in req.games:
        print(game.name, f'https://{game.cover.url.replace("t_thumb", "t_1080p")}')
    
        
    return render_template('index.html', title = "Welcome!",
                           game_list = req.games)