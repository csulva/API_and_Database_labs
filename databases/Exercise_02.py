#Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

import re
import sqlalchemy
from pprint import pprint

from sqlalchemy.sql.expression import join

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#Select all the actors with the first name of your choice
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.select([actor]).where(actor.columns.first_name=='PENELOPE')
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# pprint(result)

#Select all the actors and the films they have been in
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# query = sqlalchemy.select([actor.columns.actor_id, actor.columns.first_name, actor.columns.last_name, film.columns.title]).select_from(join_statement)
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# pprint(result)

#Select all the actors that have appeared in a category of a comedy of your choice

#Select all the comedic films and sort them by rental rate

#Using one of the statements above, add a GROUP BY statement of your choice

#Using one of the statements above, add a ORDER BY statement of your choice

