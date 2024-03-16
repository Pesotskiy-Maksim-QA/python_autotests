import requests
import pytest

#Тест на проверку статус кода 200
def test_status_code_trainers():
    token = '' 
    response = requests.get('https://api.pokemonbattle.me/v2/trainers', params={"trainer_id": 397})
    assert response.status_code == 200

#Тест проверку статус кода 200 при отправке запроса, и при получение нужных данных
def test_trainer_name():
    token = ''
    response = requests.get('https://api.pokemonbattle.me/v2/trainers', params={'trainer_id': 397})
    response_body = response.json()
    #assert response.status_code == 200
    assert response_body == 'Максимус'
