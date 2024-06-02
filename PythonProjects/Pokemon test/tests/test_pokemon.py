import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3271b76b466b4b674886c21d15e636fa'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4064'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : '4064'})
    assert response_get.json()["data"][0]["trainer_name"] == 'Панда'

