from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String

Base = declarative_base()

# CREATE TABLE pony_handlers (
#   pony_id INTEGER NOT NULL,
#   handler_id INTEGER NOT NULL,
#   PRIMARY KEY (pony_id, handler_id),
#   FOREIGN KEY (pony_id) REFERENCES ponies(id),
#   FOREIGN KEY (handler_id) REFERENCES handlers(id)
# );
pony_handlers = Table(
    "pony_handlers",
    Base.metadata,
    Column("pony_id", ForeignKey("ponies.id"), primary_key=True),
    Column("handler_id", ForeignKey("handlers.id"), primary_key=True))

# Pony and Owner declarations below...

class Owner(Base):
    # declares the tablename in the db
    __tablename__ = "owners"

    # declares the columns in the table
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))

    # sets up rlelationship many-one-relationship
    ponies = relationship("Pony", back_populates="owner")


class Pony(Base):
    __tablename__ = "ponies"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birth_year = Column(Integer)
    breed = Column(String(255))
    owner_id = Column(Integer, ForeignKey("owners.id"))

    owner = relationship("Owner", back_populates="ponies")

    
    # sets up many to many
    handlers = relationship("Handler",
                            secondary=pony_handlers,
                            back_populates="ponies")
    
class Handler(Base):
    __tablename__ = "handlers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    employee_id = Column(String(12))

    ponies = relationship("Pony",
                          secondary=pony_handlers,
                          back_populates="handlers")