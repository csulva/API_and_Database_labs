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

from sqlalchemy.sql.expression import asc, text

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
5. Add new column to table
6. Delete data from a table
7. View users posts
''')


# Functions
# 1
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

# 2
def create_table():
    global metadata
    name_table = input('Please name your table: ')
    print(f'Your new table is called {name_table}. It will have a primary key column titled {name_table}_id.')
    time.sleep(1)
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
                data_type = sqlalchemy.Integer()
            elif data_type == 'float':
                data_type = sqlalchemy.Float()
            elif data_type == 'string':
                length = input('How long would you like your string to be, maximum? Type a number: ')
                data_type = sqlalchemy.String(int(length))
            elif data_type == 'bool':
                data_type = sqlalchemy.Boolean()
            new_table = sqlalchemy.Table(f'{name_table}', metadata,
                sqlalchemy.Column(f'{name_table}_id', sqlalchemy.Integer()),
                sqlalchemy.Column(column_1, data_type, nullable=False))
            print(f'Executing new table {name_table}...')
            metadata.create_all(engine)
            list_of_tables.append(new_table)
            time.sleep(2)
            print(f'You successfully created a {name_table} table. To add data to it, please restart the application and select option 3. ')
            quit()

# 3
def add_data_to_table():
    print('Tables: ')
    for tables in list_of_tables:
        print(tables)
    select_table = input('Which table would you like to add data to? ')

    # pprint(repr(metadata.tables[select_table].columns.keys()))
    if select_table == 'Users':
        first_name = input("What's the first name? ")
        last_name = input("What's the last name? ")
        email = input("What's the email address? ")
        query = sqlalchemy.insert(users).values(UserId = 101, FirstName=first_name, LastName=last_name, Email=email)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Images':
        url = input("What's the url of the image you would like to post? ")
        query = sqlalchemy.insert(images).values(ImageId = 101, ImageURL=url)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Posts':
        post_text = input('Please enter the text of your post: ')
        query = sqlalchemy.insert(posts).values(PostID = 201, UserID = 2, PostText = post_text, ImageID = 301)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Users_Friends':
        friendship_id = input("What's your App ID? Enter a positive integer: ")
        mutual_friend = input('Who do you want to be friends with? Enter their App ID: ')
        query = sqlalchemy.insert(users_friends).values(ID = 201, UserID_1 = friendship_id, UserID_2 = mutual_friend)
        results_proxy = connection.execute(query)
        print('Success!')
        quit()
    while select_table != 'Users' or select_table != 'Images' or select_table != 'Posts' or select_table != 'Users_Friends':  
        print('\nType in the correct table name from the list below.')
        add_data_to_table()
    quit()

# 4
def update_table_data():
    print('Tables: ')
    for tables in list_of_tables:
        print(tables)
    select_table = input('Which table would you like to update data for? ')
    if select_table == 'Users':
        email_question = input("Let's look you up based on email... what is your email address? ")
        print("OK, now let's update your user information...")
        time.sleep(1)
        first_name = input("What's your first name? ")
        last_name = input("What's your last name? ")
        email = input("What's your email address? ")
        query = sqlalchemy.update(users).values(FirstName=first_name, LastName=last_name, Email=email).where(users.columns.Email == email_question)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Images':
        new_image = input('Which number image would you like to change? ')
        url = input("What image would you like to change it to? Enter URL: ")
        query = sqlalchemy.update(images).values(ImageURL=url).where(images.columns.ImageId == new_image)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Posts':
        post_number = input("Which number post would you like to edit? ")
        post_text = input('Please enter the new text of your post: ')
        query = sqlalchemy.update(posts).values(PostText = post_text).where(posts.columns.ImageID == post_number)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Users_Friends':
        friendship_id = input("What's your App ID? Enter a positive integer: ")
        unfriend = input('Who would you like to "unfriend"? Enter their App ID: ')
        mutual_friend = input('Who would you like to be friends with instead? Enter their App ID: ')
        query = sqlalchemy.update(users_friends).values(UserID_1 = friendship_id, UserID_2 = mutual_friend).where(users_friends.columns.UserID_1 == friendship_id and users_friends.columns.UserID_2 == unfriend)
        results_proxy = connection.execute(query)
        print('Success!')
        quit()
    while select_table != 'Users' or select_table != 'Images' or select_table != 'Posts' or select_table != 'Users_Friends':  
        print('\nType in the correct table name from the list below.')
        add_data_to_table()
    quit()

# 5
def add_column():
    print('Tables: ')
    for tables in list_of_tables:
        print(tables)
    select_table = input('Which table would you like to add a column to? ')
    selected_table = sqlalchemy.Table(f'{select_table}', metadata, autoload=True, autoload_with=engine)
    column_name = input('What would you like to name the column? ')
    data_type = input('What is the datatype of this column? Type "int" for integer, "float" for a floating number, "string" for string, or "bool" for a boolean value. ')
    if data_type == 'int':
        data_type = sqlalchemy.Integer()
    elif data_type == 'float':
        data_type = sqlalchemy.Float()
    elif data_type == 'string':
        length = input('How long would you like your string to be, maximum? Type a number: ')
        data_type = sqlalchemy.String(int(length))
    elif data_type == 'bool':
        data_type = sqlalchemy.Boolean()
    new_column = sqlalchemy.Column(column_name, data_type)
    print(f'Creating new column {column_name} in table {selected_table}')
    # new_new_column = images.append_column(new_column)
    query = sqlalchemy.update(selected_table).values(new_column)
    results_proxy = connection.execute(query)
    metadata.create_all(engine)
    quit()

# 6
def delete_data():
    print('Tables: ')
    for tables in list_of_tables:
        print(tables)
    select_table = input('Which table would you like to delete data from? ')
    if select_table == 'Users':
        email_question = input("Let's delete your info based on your email... what is your email address? ")
        print("OK, now let's delete your user information...")
        time.sleep(1)
        query = sqlalchemy.delete(users).where(users.columns.Email == email_question)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Images':
        new_image = input('Which number would you like to delete? Please enter the image number: ')
        print("OK, now deleting the image...")
        query = sqlalchemy.delete(images).where(images.columns.ImageId == new_image)
        result_proxy = connection.execute(query)
        time.sleep(1)
        print('Success!')
        quit()
    elif select_table == 'Posts':
        post_number = input("Which post would you like to delete? Enter the image number: ")
        query = sqlalchemy.delete(posts).where(posts.columns.ImageID == post_number)
        print("OK, now deleting the image...")
        time.sleep(1)
        result_proxy = connection.execute(query)
        print('Success!')
        quit()
    elif select_table == 'Users_Friends':
        friendship_id = input("What's your App ID? Enter a positive integer: ")
        unfriend = input('Who would you like to "unfriend"? Enter their App ID: ')
        query = sqlalchemy.delete(users_friends).where(users_friends.columns.UserID_1 == friendship_id and users_friends.columns.UserID_2 == unfriend)
        print("OK, now deleting your friendship...")
        time.sleep(1)
        results_proxy = connection.execute(query)
        print('Success!')
        quit()
    while select_table != 'Users' or select_table != 'Images' or select_table != 'Posts' or select_table != 'Users_Friends':  
        print('\nType in the correct table name from the list below.')
        add_data_to_table()
    quit()

# 7
def view_users_posts():
    join_statement = posts.join(users, posts.columns.UserID == users.columns.UserId)
    # join = join_statement.join(posts, users.columns.UserId == posts.columns.UserID)
    query = sqlalchemy.select(users.columns.UserId, users.columns.FirstName, users.columns.LastName, posts.columns.PostText).select_from(join_statement).order_by(sqlalchemy.asc(users.columns.UserId))
    results_proxy = connection.execute(query)
    results = results_proxy.fetchall()
    pprint(results)
    quit()

# Application Rules
while user_input:
    if user_input == '1':
        show_data()
    if user_input == '2':
        create_table()
    if user_input == '3':
        add_data_to_table()
    if user_input == '4':
        update_table_data()
    if user_input == '5':
        add_column()
    if user_input == '6':
        delete_data()
    if user_input == '7':
        view_users_posts()
