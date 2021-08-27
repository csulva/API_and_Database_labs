'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

print('film:')
print(film.columns.keys())
print(repr(metadata.tables['film']))
print('category:')
print(category.columns.keys())
print(repr(metadata.tables['category']))

#query = sqlalchemy.select([film])

# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()

# pprint(result_set)