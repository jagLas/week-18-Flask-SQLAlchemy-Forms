from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
engine = create_engine(db_url)

SessionFactory = sessionmaker(bind=engine)

session = SessionFactory()

# Do stuff with the session

engine.dispose()