import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3271b76b466b4b674886c21d15e636fa'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Kukusik",
    "photo": "https://dolnikov.ru/pokemons/albums/118.png"
}

body_rename = {
    "pokemon_id": "26937",
    "name": "Kukusik44",
    "photo": "https://dolnikov.ru/pokemons/albums/013.png"
}

body_add_pokeball = {
    "pokemon_id": "26938"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)
