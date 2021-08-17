'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
url = 'http://demo.codingnomads.co:8080/tasks_api/users'

body = {
'id': 404,
'first_name': "Error",
'last_name': "Code",
'email': "404error@gmail.com",
}

response = requests.put(url, json=body)

print(f'Response Code: {response.status_code}')

response = requests.get(url, json=body)

print(f"Response Content: {response.content}")