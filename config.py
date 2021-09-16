import os

class Config:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("DEVELOPMENT")
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True