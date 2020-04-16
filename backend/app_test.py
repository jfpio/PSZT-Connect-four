import pytest
import json

from backend.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        app.debug = True
        yield client


def test_game_initialize(client):
    input_data = {
        'board': [[0 for x in range(7)] for y in range(6)],
        'depth': 10,
    }
    excepted_data = [[0 for x in range(7)] for y in range(6)]

    response = client.post('/', data=json.dumps(input_data), content_type='application/json')
    output_data = json.loads(response.data)
    assert output_data == excepted_data
