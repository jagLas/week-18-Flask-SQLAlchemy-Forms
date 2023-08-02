from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Owner, Pony, Handler

db_url = "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
engine = create_engine(db_url)

SessionFactory = sessionmaker(bind=engine)

session = SessionFactory()


# Do stuff with the session

# # commented stuff below to create a new entry
# you = Owner(first_name="your first name",
#             last_name="your last name",
#             email="your email")

# your_pony = Pony(name="your pony's name",
#                  birth_year=2020,
#                  breed="whatever you want",
#                  owner=you)

# print(you.id)         # > None
# print(your_pony.id)   # > None

# session.add(you)
# session.commit()

# print(you.id)         # > 4 (or whatever the new id is)
# print(your_pony.id)   # > 4 (or whatever the new id is)


# # commented stuff below updates a record
# your_pony = session.query(Pony).get(5)
# print(your_pony.birth_year)

# your_pony.birth_year = 2019
# print(your_pony.birth_year)

# session.commit()


# # to rollback before a commit
# your_pony.name = "Mr. Fancy Pants"
# your_pony.birth_year = 1896
# print(your_pony.name)
# print(your_pony.birth_year)

# session.rollback()
# print(your_pony.name)
# print(your_pony.birth_year)

# # To delete a record
# you = session.query(Owner).get(7)
# print(you.first_name)
# session.delete(you)
# session.commit()

session.close()

engine.dispose()