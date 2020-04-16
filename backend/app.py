from flask import Flask
from flask import request
from backend.game import get_ai_move

app = Flask(__name__)


@app.route('/', methods=['POST'])
def game():
    if request.method == 'POST':
        return get_ai_move()


if __name__ == '__main__':
    app.run(debug=True)
