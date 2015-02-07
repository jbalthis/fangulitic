#!/usr/bin/env python2

from flask import Flask, Blueprint
from app.users import users
from app.dashboard import dashboard
from app.astores import astores
from app.customs import customs
from app.replicated import replicated
from app.wordpress import wordpress
from app.verifyakey import verifyakey
from app import app


app.register_blueprint(users)
app.register_blueprint(dashboard)
app.register_blueprint(astores)
app.register_blueprint(customs)
app.register_blueprint(replicated)
app.register_blueprint(wordpress)
app.register_blueprint(verifyakey)

if __name__ == '__main__':
    app.run()
