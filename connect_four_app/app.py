from flask import Flask, session
from flask import request

from connect_four_app.config import SECRET_KEY
from connect_four_app.game import game_initialize, opponent_turn, get_game_results

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        return game_initialize()
    elif request.method == 'GET':
        get_game_results()


if __name__ == '__main__':
    app.run(debug=True)
