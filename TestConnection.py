# Author: Steve Nelson
# Description: Test Connection to local PostgreSQL database
# File: TestConnection.py
# Date: 11/23/2021
#
# Notes:
#
# Parameters:
#    None
#
# Imports
import psycopg2
import Commands

# Try and Catch block
try:
    # Create a connection the PostgreSQL database. Use the default database.
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password=Commands.PWD)  # Replace <password> with your own password during installation

    print('Database connection created.')

    # Create a database cursor
    cursor = connection.cursor()

    # Execute a statement
    cursor.execute('SELECT version()')

    # Fetch One Row which should be the database version
    db_version = cursor.fetchone()

    # Print Database Version
    print('Database version is: ', db_version)

    # If the connection is open, close it.
    if connection is not None:
        connection.close()
        print('Database connection closed.')

except (Exception, psycopg2.DatabaseError) as error:
    print('Error: ', error)
