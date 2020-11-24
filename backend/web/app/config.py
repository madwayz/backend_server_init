import os

DATABASE = {
    "dbname": os.environ.get('POSTGRES_DB'),
    "user": os.environ.get('POSTGRES_USER'),
    "host": 'postgres',
    "password": os.environ.get('POSTGRES_PASSWORD')
}


class Config:
    JSON_AS_ASCII = False