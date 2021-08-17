'''
Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.
'''

new_input = input('''Greetings, please select an action:
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
''')

import requests
url = 'http://demo.codingnomads.co:8080/tasks_api/users'

def new_account_1(x, y, z):
    body = {
    'id': 100,
    'first_name': x,
    'last_name': y,
    'email': z,
    }
    requests.post(url, json=body)
    print(requests.post(url, json=body).status_code)

def delete_task(x):
    response = requests.delete(url + f'/{x}')
    print(response.status_code)
    if response.status_code == '404':
        print('404 error... please try again')
        quit()

#while new_input == True:
if new_input == '1':
    x = input('What is your first name? ')
    x = x
    y = input('What is your last name? ')
    y = y
    z = input('What is your email address? ')
    z = z
    new_account_1(x, y, z)

if new_input == '7':
    x = input('What is your ID number? ')
    delete_task(x)
