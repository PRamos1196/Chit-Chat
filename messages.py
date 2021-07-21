import flask_sqlalchemy
from app import db
from enum import Enum


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(14))
    message = db.Column(db.String(500))
    imageUrl = db.Column(db.String(500))

    def __init__(self, u, m, i):
        self.username = u
        self.message = m
        self.imageUrl = i


db.create_all()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))

    def __init__(self, u):
        self.username = u


db.create_all()


class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))
    email = db.Column(db.String(500))
    imageUrl = db.Column(db.String(500))

    def __init__(self, name, email, imageUrl, auth_type):
        assert type(auth_type) is AuthUserType
        self.name = name
        self.email = email
        self.imageUrl = imageUrl
        self.auth_type = auth_type.value

    def __repr__(self):
        return "<User name: {}\nAuth type: {}".format(self.name, self.auth_type)


db.create_all()


class AuthUserType(Enum):
    GOOGLE = "google"
