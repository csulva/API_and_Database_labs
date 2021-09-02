'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import sqlalchemy
from pprint import pprint
import requests

# from sqlalchemy.sql.ddl import CreateSchema

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/API_Data')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#engine.execute(sqlalchemy.schema.CreateSchema('API_Data'))

url = 'http://demo.codingnomads.co:8080/tasks_api/users'

id_numbers = []
first_names = []
last_names = []
emails = []

response = requests.get(url)
email = response.json()
for key, value in email.items():
    if key == 'data':
        new_value = value
        for dict in new_value[0::]:
            for key, value in dict.items():
                if key == 'id':
                    id_numbers.append(int(value))
                if key == 'first_name':
                    first_names.append(value)
                if key == 'last_name':
                    last_names.append(value)
                if key == 'email':
                    emails.append(value)
                
new_table = sqlalchemy.Table(f'User_Data', metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(100), nullable=True),
    sqlalchemy.Column('last_name', sqlalchemy.String(100), nullable=True),
    sqlalchemy.Column('email_address', sqlalchemy.String(100), nullable=True)
    )
#metadata.create_all(engine)

user_data = sqlalchemy.Table('User_Data', metadata, autoload=True, autoload_with=engine)

zero = 0
for x in range(0, len(id_numbers)):
    query = sqlalchemy.insert(user_data).values(user_id = id_numbers[zero], first_name = first_names[zero], last_name = last_names[zero], email_address = emails[zero])
    zero = zero + 1
    result_proxy = connection.execute(query)
