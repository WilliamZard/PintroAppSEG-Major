from flask import Config


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
