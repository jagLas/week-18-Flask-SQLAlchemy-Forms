from app import db


class Pony(db.Model):
    __tablename__ = 'ponies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    birth_year = db.Column(db.Integer)
    breed = db.Column(db.String(255))
