from flask import Flask, Blueprint, g, redirect, render_template, \
        request, url_for

dashboard = Blueprint('dashboard', __name__)


from app.modules.dashboard import forms, decorators, views, routes, models
