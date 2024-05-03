import requests

def get_url_pokemons(url):
    """Obtiene la respuesta de la url que se le pasa por parametro y la devuelve en formato json"""
    """se obtiene los datos de los pokemons"""
    response = requests.get(url)
    return response.json()

def get_url_pokemon_img(url):
    """se obtienen las url de las imagenes de los pokemons"""
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = get_url_pokemons(url)
    # busco el la respuesta de la url la key 'results' que contiene los datos que necesito mostrar
    # data = response['results']
    # print(response)
    # print(len(response['results']))

# for i in data:
#     # print(i['name'])
#     url = i['url']
#     response = get_url_pokemon_img(url)
#     url_img = response['sprites']['other']['dream_world']['front_default']







