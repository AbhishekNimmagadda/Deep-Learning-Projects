import os
'''
class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@3.80.146.128:5432/abhi-db')
'''
class DevelopmentConfig:
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@3.80.146.128:5432/abhi-db')
'''
class DevelopmentConfig:
    DEBUG = True
    # Add other configuration variables as needed

'''
'''
class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://user:password@localhost:5432/stock_db')
class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://user:password@localhost:5432/stock_db_test')
'''
