import psycopg2
from core.config import *

def PGconnection():
    with psycopg2.connect(
        host = PGHOST,
        user = PGUSER,
        password = PGPASSWORD,
        database = PGDATABASE,
        port = PGPORT) as connection:
        connection.autocommit = True
    return connection
    

def CheckRegister(user_id):
    with PGconnection().cursor() as cursor:
        cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
        usercheck = cursor.fetchone()
        return usercheck


def RegistrationUserPG(user_id, username, first_name, last_name, phone):
    with PGconnection().cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (\
                id SERIAL PRIMARY KEY,\
                user_id BIGINT NOT NULL,\
                username VARCHAR(50) DEFAULT 'NOT username',\
                first_name VARCHAR(250) DEFAULT 'NOT first_name',\
                last_name VARCHAR(250) DEFAULT 'NOT last_name',\
                phone VARCHAR(50) NOT NULL,\
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        if CheckRegister(user_id) is None:
            cursor.execute(
                        "INSERT INTO users (user_id, username, first_name, last_name, phone) \
                        VALUES (%s,  %s, %s, %s, %s)", (user_id, username, first_name, last_name, phone))
        else:
            pass
            
        
        
