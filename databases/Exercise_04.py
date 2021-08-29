'''
Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!
'''
import sqlalchemy
from pprint import pprint
import time

from sqlalchemy.sql.expression import null

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/SocialDB')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Tables
images = sqlalchemy.Table('Images', metadata, autoload=True, autoload_with=engine)
posts = sqlalchemy.Table('Posts', metadata, autoload=True, autoload_with=engine)
users = sqlalchemy.Table('Users', metadata, autoload=True, autoload_with=engine)
users_friends = sqlalchemy.Table('Users_Friends', metadata, autoload=True, autoload_with=engine)

list_of_tables = [images, posts, users, users_friends]

# User Input
print('Welcome to my database application with sqlalchemy. ')
time.sleep(2)
user_input = input('''Please select your task:
1. Show data in a table
2. Create a new table
3. Add data to a table
4. Update data in a table
5. Delete data from a table
6. Delete a table
7. Compare data between two tables
''')

# Functions
def show_data():
    new_input = input(f'For which data would you like to view the data?\n1. {list_of_tables[0]}\n2. {list_of_tables[1]}\n3. {list_of_tables[2]}\n4. {list_of_tables[3]}\n')
    while new_input == '1' or new_input == '2' or new_input == '3' or new_input == '4':
        if new_input == '1':
            query = sqlalchemy.select([images])
            results_proxy = connection.execute(query)
            results = results_proxy.fetchall()
            pprint(results)
            quit()
        elif new_input == '2':
            query = sqlalchemy.select([posts])
            results_proxy = connection.execute(query)
            results = results_proxy.fetchall()
            pprint(results)
            quit()
        elif new_input == '3':
            query = sqlalchemy.select([users])
            results_proxy = connection.execute(query)
            results = results_proxy.fetchall()
            pprint(results)
            quit()
        elif new_input == '4':
            query = sqlalchemy.select([users_friends])
            results_proxy = connection.execute(query)
            results = results_proxy.fetchall()
            pprint(results)
            quit()
        else:
            new_input == new_input

def create_table():
    global metadata
    name_table = input('Please name your table: ')
    print(f'Your new table is called {name_table}. It will have a primary key column titled {name_table}_id.')
    new_column = input(f'Would you like to create a new column for {name_table} table? Type "yes" to create a new column. Type "no" or "quit" to stop. ')
    if new_column == 'quit'.lower() or new_column == 'no'.lower():
        new_table = sqlalchemy.Table(f'{name_table}', metadata,
    sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()))
        metadata.create_all(engine)
        list_of_tables.append(name_table)
        print(f'You created a {name_table} table. To add data to it, please restart the application and select option 3. ')
        quit()
    else:
        column_1 = input('Please name your next column (type "quit" and click enter to stop): ')
        if column_1 == 'quit'.lower() or new_column == 'no'.lower():
            new_table = sqlalchemy.Table(f'{name_table}', metadata,
    sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()))
            metadata.create_all(engine)
            list_of_tables.append(name_table)
            print(f'You created a {name_table} table. To add data to it, please restart the application and select option 3. ')
            quit()
        else:
            data_type = input('What is the datatype of this column? Type "int" for integer, "float" for a floating number, "string" for string, or "bool" for a boolean value. ')
            if data_type == 'int':
                new_table = sqlalchemy.Table(f'{name_table}', metadata,
                sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()),
                sqlalchemy.Column(column_1, sqlalchemy.Integer(), nullable=False))
                metadata.create_all(engine)
                list_of_tables.append(name_table)
                print(f'You created a {name_table} table. To add data to it, please restart the application and select option 3. ')
                quit()
            elif data_type == 'float':
                new_table = sqlalchemy.Table(f'{name_table}', metadata,
                sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()),
                sqlalchemy.Column(column_1, sqlalchemy.Float(), nullable=False))
                metadata.create_all(engine)
                list_of_tables.append(name_table)
                print(f'You created a {name_table} table. To add data to it, please restart the application and select option 3. ')
                quit()
            elif data_type == 'string':
                length = input('How long would you like your string to be, maximum? Type a number: ')
                length = int(length)
                new_table = sqlalchemy.Table(f'{name_table}', metadata,
                sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()),
                sqlalchemy.Column(column_1, sqlalchemy.String(length), nullable=False))
                metadata.create_all(engine)
                list_of_tables.append(name_table)
                print(f'You created a {name_table} table. To add data to it, please restart the application and select option 3. ')
                quit()
            elif data_type == 'bool':
                new_table = sqlalchemy.Table(f'{name_table}', metadata,
                sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()),
                sqlalchemy.Column(column_1, sqlalchemy.Boolean(), nullable=False))
                metadata.create_all(engine)
                list_of_tables.append(name_table)
                print(f'You created a {name_table} table. To add data to it, please restart the application and select option 3. ')
                quit()


while user_input:
    if user_input == '1':
        show_data()
    if user_input == '2':
        create_table()