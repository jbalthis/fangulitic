from flask import Flask
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(140))
    theme = db.Column(db.String(12))
    admin = db.Column(db.Boolean())

    def __init__(self, username, password, theme, admin):
        self.username = username
        self.password = password
        self.theme = theme
        self.admin = admin

    def is_admin():
        return self.admin
