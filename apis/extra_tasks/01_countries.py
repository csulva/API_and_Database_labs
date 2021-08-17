'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
import pprint
import json
import requests

argentina = 'https://restcountries.eu/rest/v2/name/argentina'

usa = 'https://restcountries.eu/rest/v2/name/usa'

response_1 = requests.get(usa).text
response_1 = json.loads(response_1)

response_2 = requests.get(argentina).text
response_2 = json.loads(response_2)

response_dict = response_1[0]
dict_2 = response_2[0]

for key, value in response_dict.items():
    if key == 'population':
        print(f'population of United States: {value}')
# for key, value in response.items():
#     pprint.pprint(key, value)
for key, value in dict_2.items():
    if key == 'population':
        print(f'population of Argentina: {value}')
