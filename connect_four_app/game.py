import json
from flask import session, request, jsonify

from connect_four_app.players import Players


def game_initialize():
    data = request.get_json()
    state = {
        'turn': data['turn'],
        'depth': data['depth'],
        'board': [[Players.NOBODY.value for x in range(7)] for y in range(6)],
        'winner': Players.NOBODY.value
    }
    session['state'] = json.dumps(state)
    return jsonify(state)


def opponent_turn():
    pass


def get_game_results():
    pass
