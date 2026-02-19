from Flasky import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    password=db.Column(db.String(20))

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, unique=True)
    link=db.Column(db.String, unique=True)