from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Owner, Pony, Handler
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db_url = "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
engine = create_engine(db_url)

SessionFactory = sessionmaker(bind=engine)

session = SessionFactory()


# pony_query = session.query(Pony)
# print(pony_query)

# pony_id_3_query = session.query(Pony).get(3)
# print(pony_id_3_query.name, pony_id_3_query.birth_year, pony_id_3_query.breed)

# owner_query = session.query(Owner.first_name, Owner.last_name).order_by(Owner.last_name).all()
# print(owner_query)

# pony_query = session.query(Pony).filter(Pony.name.like('%u%'))
# for pony in pony_query:
#     print(pony.name)
# print(pony_query.count())

# join allows you to filter, but does not eager load
hirzai_owners = session.query(Owner) \
                        .join(Pony) \
                        .filter(Pony.breed == 'Hirzai')

for owner in hirzai_owners:
    print(owner.first_name, owner.last_name)
    for pony in owner.ponies:
        print("\t", pony.name)

# eager loaded
hirzai_owners_and_ponies = session.query(Owner) \
                                  .join(Pony)  \
                                  .filter(Pony.breed == "Hirzai") \
                                  .options(joinedload(Owner.ponies))
for owner in hirzai_owners_and_ponies:
    print(owner.first_name, owner.last_name)
    for pony in owner.ponies:
        print("\t", pony.name)

# # lazy loading
# for owner in session.query(Owner):
#     print(owner.first_name, owner.last_name)
#     for pony in owner.ponies:
#         print("\t", pony.name)


# # eager loading
# owners_and_ponies = session.query(Owner).options(joinedload(Owner.ponies))
# for owner in owners_and_ponies:
#     print(owner.first_name, owner.last_name)
#     for pony in owner.ponies:
#         print("\t", pony.name)

session.close()

engine.dispose()