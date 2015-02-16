"""
    config - config.py
    the main application configuration file
"""

import os
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

    MONGODB_SETTINGS = 'host=mongodb://localhost:27017/fangulitic_dev_db'
    MONGOALCHEMY_DATABASE = 'fangulitic_dev_db'
    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        # 'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        # 'flask_debugtoolbar.panels.logger.LoggingDebugPanel',
        'flask_debugtoolbar_mongo.panel.MongoDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    ]
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfig(Config):
    MONGODB_SETTINGS = 'host=mongodb://localhost:27017/fangulitic_db'


config = {

    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
