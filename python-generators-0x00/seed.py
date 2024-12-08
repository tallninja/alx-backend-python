#!/usr/bin/env python3

from mysql.connector import connect, Error

DB_HOST = 'localhost'
DB_USER = 'admin'
DB_PASSWORD = 'password'
DB_NAME = 'ALX_prodev'

def connect_db():
    try:
        with connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD) as connection:
            print(connection)
            return connection
    except Error as e:
        print(e)


def create_database(connection):
    query = f'CREATE DATABASE IF NOT EXISTS {DB_NAME}'
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
    except Error as e:
        print(e)


def conect_to_prodev():
    try:
        with connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME) as connection:
            return connection
    except Error as e:
        print(e)


def create_table(connection):
    query = '''CREATE TABLE IF NOT EXISTS (
                user_id VARCHAR(255) PRIMARY KEY, 
                name VARCHAR NOT NULL, 
                email VARCHAR NOT NULL,
                age DECIMAL NOT NULL
            )'''
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
    except Error as e:
        print(e)


if __name__ == '__main__':
    connection = connect_db()
    create_database(connection)

