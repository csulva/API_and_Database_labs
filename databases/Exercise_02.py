#Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:
import sqlalchemy
from sqlalchemy import func
from pprint import pprint


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

# join_statement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# query = sqlalchemy.select([actor.columns.actor_id, actor.columns.first_name, actor.columns.last_name, film.columns.title]).select_from(join_statement)
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# pprint(result)

#Select all the actors that have appeared in a category of your choice

category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

# join_statement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# new_join = join_statement.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
# query = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, film.columns.title, category.columns.name]).select_from(new_join).where(category.columns.name == "comedy")
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# pprint(result)

#Select all the comedic films and sort them by rental rate
rental = sqlalchemy.Table('rental', metadata)
inventory = sqlalchemy.Table('inventory', metadata, autoload=True, autoload_with=engine)
# join_statement = category.join(film_category, category.columns.category_id == film_category.columns.category_id).join(film, film.columns.film_id == film_category.columns.film_id)
# new_join = join_statement.join(inventory, inventory.columns.film_id == film.columns.film_id).join(rental, rental.columns.inventory_id == inventory.columns.inventory_id)
# query = sqlalchemy.select([film.columns.title, sqlalchemy.func.sum(rental.columns.inventory_id)]).select_from(new_join).where(category.columns.name == 'comedy')
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# pprint(result)

#Using one of the statements above, add a GROUP BY statement of your choice

join_statement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([sqlalchemy.func.count(film.columns.title), actor.columns.first_name, actor.columns.last_name]).select_from(join_statement).group_by(actor.columns.first_name, actor.columns.last_name).order_by(sqlalchemy.desc(sqlalchemy.func.count(film.columns.title)))
result_proxy = connection.execute(query)
result = result_proxy.fetchall()
pprint(result)

#Using one of the statements above, add a ORDER BY statement of your choice

# join_statement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# query = sqlalchemy.select([actor, film]).select_from(join_statement).order_by(sqlalchemy.asc(film.columns.title))
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
# pprint(result)