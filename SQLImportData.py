# Author: Steve Nelson
# Description: Connection to local PostgreSQL database and create a database
# File: SQLImportData.py
# Date: 11/23/2021
#
# Notes:
#   12/1/2021 SDN - Fix problem with conversion to CSV for importing.
#
# Parameters:
#    None
#
# Imports
from io import StringIO
import csv
import pandas as pan
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Commands

# Constants
INPUT_FILE = "netflix_titles.csv"  # Input file

# Try and Catch block
try:
    # Read the file in a pandas formatted stream
    data = pan.read_csv(INPUT_FILE)

    if data is not None:

        # Create a connection the PostgreSQL database. Use the new database.
        connection = psycopg2.connect(
            host="localhost",
            database="netflix",
            user="postgres",
            password=Commands.PWD)  # Replace <password> with your own password during installation

        # Set the database connection characteristics
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        connection.set_client_encoding("UTF8")

        if connection is not None:
            print('Database connection created.')

        # Create a database cursor
        cursor = connection.cursor()

        # Convert the Pandas data to a StringIO array
        serverio = StringIO()
        serverio.write(data.to_csv(index=False, header=False, quoting=csv.QUOTE_NONNUMERIC, sep=','))
        serverio.seek(0)

        # Copy the data to the database in a CSV format managing the double quotes and the semicolon.
        cursor.copy_expert("""COPY shows FROM STDIN WITH (FORMAT CSV)""", serverio)

        # Fetch the rowcount
        db_return = cursor.rowcount

        # Print Database Information
        print('Database returned: ', db_return)

        # If the connection is open, close it.
        if connection is not None:
            connection.close()
            print('Database connection closed.')
    else:
        print('Could not open the file.')

except (Exception, psycopg2.DatabaseError) as error:
    print('Error: ', error)
