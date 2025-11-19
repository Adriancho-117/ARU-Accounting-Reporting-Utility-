import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",        # tu contraseña si tienes
            database="contabilidad_db"
        )
        return conn
    except Error as e:
        print("Error:", e)
        return None



