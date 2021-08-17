'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
url = 'http://demo.codingnomads.co:8080/tasks_api/users'
list_of_emails = []

response = requests.get(url)
email = response.json()
for key, value in email.items():
    if key == 'data':
        new_value = value
        for dict in new_value[0::]:
            for key, value in dict.items():
                if key == 'email':
                    list_of_emails.append(value)
print(list_of_emails)