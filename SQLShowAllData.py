# Author: Steve Nelson
# Description: Connection to local PostgreSQL database and table and list all the data
# File: SQLShowAllData.py
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
        database="netflix",
        user="postgres",
        password=Commands.PWD)  # Replace <password> with your own password during installation

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    print('Database connection created.')

    # Create a database cursor
    cursor = connection.cursor()

    # Execute a statement
    cursor.execute(Commands.SELECTALLDATA)

    # Fetch One Row which should be the database version
    db_rows = cursor.fetchall()

    # Print Database Rows / Print out the column names
    print('Database returned:')
    for row in db_rows:
        print(row)

    # If the connection is open, close it.
    if connection is not None:
        connection.close()
        print('Database connection closed.')

except (Exception, psycopg2.DatabaseError) as error:
    print('Error: ', error)
