from flask import request, jsonify


def get_ai_move():
    data = request.get_json()
    board = calculate_move(data['board'])
    return jsonify(board)


def calculate_move(board):
    return board
