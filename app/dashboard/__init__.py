from flask import Flask, Blueprint, g, redirect, render_template, \
        request, url_for

dashboard = Blueprint('dashboard', __name__)

import app.dashboard.models
import app.dashboard.forms
import app.dashboard.decorators
import app.dashboard.views
