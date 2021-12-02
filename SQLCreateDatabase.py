# Author: Steve Nelson
# Description: Connection to local PostgreSQL database and create a database
# File: SQLCreateDatabase.py
# Date: 11/23/2021
#
# Notes:
#
# Parameters:
#    None
#
# Imports
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Commands

# Try and Catch block
try:
    # Create a connection the PostgreSQL database. Use the default database.
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password=Commands.PWD)  # Replace this password with your own password during installation

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    if connection is not None:
        print('Database connection created.')

    # Create a database cursor
    cursor = connection.cursor()

    # Execute a statement
    cursor.execute(Commands.CREATEDB)

    # Fetch the message. It should be "CREATE DATABASE" upon successful completion
    db_return = cursor.statusmessage

    # Print Message
    print('Database returned: ', db_return)

    # If the connection is open, close it.
    if connection is not None:
        connection.close()
        print('Database connection closed.')

except (Exception, psycopg2.DatabaseError) as error:
    print('Error: ', error)
