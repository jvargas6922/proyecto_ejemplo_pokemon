from string import Template
html_template = Template('''
<!DOCTYPE html>
<html>
    <head>
        <title>Pokemons</title>
    </head>
    <body>
        <h1>Listado de Pokemons</h1>
        $body
    </body>
</html>
''')

elem_template = Template(
'''<h1>$name</h1>
    <img src="$url">
''')