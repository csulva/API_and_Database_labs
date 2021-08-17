'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests
url = 'http://demo.codingnomads.co:8080/tasks_api/users'

body = {
'id': 455,
'first_name': "Chris",
'last_name': "Sulva",
'email': "csulva@elon.edu",
}

response = requests.post(url, json=body)

print(f'Response Code: {response.status_code}')

response = requests.get(url)

print(f"Response Content: {response.content}")