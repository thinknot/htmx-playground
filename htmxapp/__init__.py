# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('htmxapp.config.Config')

db = SQLAlchemy(app)   # flask-sqlalchemy
bc = Bcrypt(app)   # flask-bcrypt

lm = LoginManager()   # flask-loginmanager
lm.init_app(app)       # init the login manager

# Import routing, models and Start the App
from htmxapp import views, models
