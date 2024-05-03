import get_url
import template

def build_html(url):
    """Construye el html con los datos de los pokemons obtenidos de la url que se le pasa por parametro y devuelve el html construido  """
    pokemon_data = get_url.get_url_pokemons(url)
    text = ''
    for data in pokemon_data['results']:
        url = data['url']
        response = get_url.get_url_pokemon_img(url)
        url_img = response['sprites']['other']['dream_world']['front_default']
        text += template.elem_template.substitute(name=data['name'], url=url_img)
    return template.html_template.substitute(body=text)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/'
    html = build_html(url)
    # CODIGO PARA CREAR EL ARCHIVO HTML
    with open('pokemons.html', 'w') as file:
        file.write(html)