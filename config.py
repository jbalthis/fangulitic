"""
    config - config.py
    the main application configuration file
"""

import os
from flask_mongoengine.panels import MongoDebugPanel
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'RANDOM SHIT'
    APP_MAIL_SUBJECT_PREFIX = '[Fangulitic]'
    APP_MAIL_SENDER = 'Admin <admin@example.com>'
    APP_ADMIN = os.environ.get('APP_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    MONGODB_SETTINGS = {
        'db': 'fangulitic_dev_db',
        'host': 'localhost',
        'port': 27017
    }
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # DEBUG_TB_PANELS = [MongoDebugPanel]


class ProductionConfig(Config):

    MONGODB_SETTINGS = {
        'db': 'fangulitic_db',
        'host': 'localhost',
        'port': 27017
    }


config = {

    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
