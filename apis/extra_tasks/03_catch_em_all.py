'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''
import requests
import json
import pathlib
import csv

dict_of_poke_heights = {}
list_of_pokemon = []

# url = 'https://pokeapi.co/api/v2/pokemon/1/'
# response_test = requests.get(url)
# response_test = response_test.json()
# print(response_test.keys())

#list pokemon in order by number with heights
for x in range(1, 151):
       url = f'https://pokeapi.co/api/v2/pokemon/{x}/'
       response = requests.get(url)
       response = response.json()
       for key, value in response.items():
              if key == 'height':
                     dict_of_poke_heights = {f'{key}': int(value)}
              if key == 'name':
                     name_dict = {f'{key}': f'{value}'}
                     name_dict.update(dict_of_poke_heights)
                     list_of_pokemon.append(name_dict)
       x+=1
#print(list_of_pokemon)

#sort by height
sorted_heights = sorted(list_of_pokemon, key=lambda k: k['height'])
#print(sorted_heights)


data = open('/Users/christophersulva/Desktop/API_project/API_Labs/python_apis_databases/apis/extra_tasks/Pokemon_data.csv', 'w')
data.write(f'{list_of_pokemon}')
data.write('\n')
data.write(f'{sorted_heights}')
data.close()