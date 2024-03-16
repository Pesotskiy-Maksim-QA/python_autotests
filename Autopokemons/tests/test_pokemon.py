import requests
import pytest

#Тест на проверку статус кода 200
def test_status_code_trainers():
    token = 'fd14176a7a6acd08b83f2eec7f4c30a0' 
    response = requests.get('https://api.pokemonbattle.me/v2/trainers', params={"trainer_id": 397})
    assert response.status_code == 200

#Тест проверку статус кода 200 при отправке запроса, и при получение нужных данных
def test_trainer_name():
    token = 'fd14176a7a6acd08b83f2eec7f4c30a0'
    response = requests.get('https://api.pokemonbattle.me/v2/trainers', params={'trainer_id': 397})
    response_body = response.json()
    #assert response.status_code == 200
    assert response_body == 'Максимус'