"""
    config - config.py
    the main application configuration file
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# =========== #
# Base Config #
# =========== #

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'RANDOM SHIT'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    APP_MAIL_SUBJECT_PREFIX = '[Fangulitic]'
    APP_MAIL_SENDER = 'Admin <admin@example.com>'
    APP_ADMIN = os.environ.get('APP_ADMIN')

    @staticmethod
    def init_app(app):
        pass


# ================== #
# Development Config #
# ================== #

class DevelopmentConfig(Config):

    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
         'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    ]
    DEBUG_TB_INTERCEPT_REDIRECTS = False


# ============== #
# Testing Config #
# ============== #

class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


# ================= #
# Production Config #
# ================= #

class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


    config = {

    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
