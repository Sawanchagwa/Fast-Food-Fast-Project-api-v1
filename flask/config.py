import os


class Config(object):
    """main configuration class (the parent config class)."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """We confingure development to equal true"""
    DEBUG = True


class TestingConfig(Config):
    """the testing configuration and use SQLACHEMY as our relational database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    """Configs for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """we set debuging to false while still in the production phase"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}