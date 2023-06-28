# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config

# Grabs the folder where the script runs.
appdir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(appdir)
instancedir = os.path.join(basedir, 'instance')
print(f'Base: {basedir}')
print(f'Instance: {instancedir}')
print(f'Module: {appdir}')


class Config:
    CSRF_ENABLED = True

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app>/instance FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(instancedir, 'htmxplay.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
