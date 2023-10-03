#!/usr/bin/env python3
"""
filtered_logger
"""

import logging, os
import mysql.connector
from mysql.connector import Error

def filtered_logger(fields: list, redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = message.replace(
            field + '=' + message.split(separator)[1].split(';')[0], field + '=' + redaction)
    return message

def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        'name=%(name)s;action=%(action)s;%(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

def get_db():
    try:
        # Fetching the environment variables
        user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
        password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
        host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
        db_name = os.getenv('PERSONAL_DATA_DB_NAME')

        if not db_name:
            raise ValueError("PERSONAL_DATA_DB_NAME must be set in the environment.")

        # Creating the connection to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        
        if connection.is_connected():
            return connection
        else:
            raise ConnectionError("Failed to connect to the database.")

    except Error as e:
        print("Error while connecting to database:", e)
        return None

connection = get_db()

if connection:
    print("Successfully connected to the database.")
    connection.close()