import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_ENGINE = os.getenv('DATABASE_ENGINE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = int(os.getenv('DATABASE_PORT'))
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_TEST_NAME = os.getenv('DATABASE_TEST_NAME')
