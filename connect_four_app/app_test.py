import pytest
import json

from connect_four_app.app import app
from connect_four_app.players import Players


@pytest.fixture
def client():
    with app.test_client() as client:
        app.debug = True
        yield client


def test_game_initialize(client):
    input_data = {
        'turn': 1,
        'depth': 10
    }

    excepted_data = {
        'turn': Players.BLUE.value,
        'depth': 10,
        'board': [[0 for x in range(7)] for y in range(6)],
        'winner': Players.NOBODY.value
    }

    response = client.post('/', data=json.dumps(input_data), content_type='application/json')
    output_data = json.loads(response.data)
    assert output_data == excepted_data
