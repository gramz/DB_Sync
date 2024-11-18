import pyodbc
import mysql.connector
from ..config.database import SQL_SERVER_CONFIG, MYSQL_CONFIG
import logging

class SQLServerConnector:
    @staticmethod
    def connect():
        try:
            conn_str = (
                f"DRIVER={SQL_SERVER_CONFIG['driver']};"
                f"SERVER={SQL_SERVER_CONFIG['server']};"
                f"DATABASE={SQL_SERVER_CONFIG['database']};"
                f"UID={SQL_SERVER_CONFIG['username']};"
                f"PWD={SQL_SERVER_CONFIG['password']}"
            )
            return pyodbc.connect(conn_str)
        except Exception as e:
            logging.error(f"Error conectando a SQL Server: {str(e)}")
            raise

class MySQLConnector:
    @staticmethod
    def connect():
        try:
            return mysql.connector.connect(**MYSQL_CONFIG)
        except Exception as e:
            logging.error(f"Error conectando a MySQL: {str(e)}")
            raise
