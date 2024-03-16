import requests

token = '5e8388ec4db8b87a23bfe0fc4384aec8' # Token
url = 'https://api.pokemonbattle.me/v2'   # URL

responce_add_pokemon = requests.post (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
})

#Автоматизирую код, сделал сам две строчки, получаю айди нашего покемона и использую дальше в нужных местах.
response_body = responce_add_pokemon.json()
pokemon_id = response_body['id']

print(responce_add_pokemon.text)

change = requests.put (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id,
    "name": "ПикаПика",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(change.text)

add_pokeboll = requests.post (f'{url}/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id
})
print(add_pokeboll.text)