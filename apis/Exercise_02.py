'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import json
import requests
url = 'http://demo.codingnomads.co:8080/tasks_api/users'


response = requests.get(url).text
response = json.loads(response)

new_list = []

#print(response)

for key, value in response.items():
    if key == 'data':
        new_list.append(value)
print(new_list)