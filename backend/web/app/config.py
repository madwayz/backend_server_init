from os import environ

DATABASE = {
    "dbname": environ['POSTGRES_DB'],
    "user": environ['POSTGRES_USER'],
    "host": 'postgres',
    "password": environ['POSTGRES_PASSWORD']
}
