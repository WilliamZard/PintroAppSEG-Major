from flask import Config


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    ENV = 'development'
