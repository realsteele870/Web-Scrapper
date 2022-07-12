from difflib import diff_bytes
import mysql.connector
from mysql.connector import Error
import pandas as pd
pw="1234"
db ="gpu"
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_db_connection("34.136.219.87", "root", pw,db)


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_databse_query = "CREATE DATABASE gpu"
create_database(connection, create_databse_query)
#Databse already created


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


create_teacher_table = """
CREATE TABLE GpuPrices (
  gpu_name VARCHAR(255) PRIMARY KEY,
  gpu_price INT NOT NULL
  );
 """

connection = create_db_connection("34.136.219.87", "root", pw, db) # Connect to the Database
execute_query(connection, create_teacher_table) # Execute our defined query

