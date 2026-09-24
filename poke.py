import requests
url= ¨https://pokeapi.co/api/v2/pokemon/pikachu¨
respuesta= requests.get (url)
datos= respuesta.json ()
