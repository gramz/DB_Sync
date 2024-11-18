import os
from dotenv import load_dotenv

load_dotenv()

SQL_SERVER_CONFIG = {
    'driver': os.getenv('SQL_DRIVER', '{ODBC Driver 17 for SQL Server}'),
    'server': os.getenv('SQL_SERVER'),
    'database': os.getenv('SQL_DATABASE'),
    'username': os.getenv('SQL_USERNAME'),
    'password': os.getenv('SQL_PASSWORD')
}

MYSQL_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}
