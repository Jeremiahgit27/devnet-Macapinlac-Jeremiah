import requests 
import random
import json 


pokemon_1 = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
pokemon_2 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pokemon_3 = requests.get("https://pokeapi.co/api/v2/pokemon/gengar")

list = [{pokemon_1.content}, {pokemon_2.content}, {pokemon_3.coontent}]
random.shuffle(list)
random_powpow = list[:1]
guess_powpow = (random_powpow)

