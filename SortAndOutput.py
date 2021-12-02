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
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, AsIs
import Commands

# Constant
OUTPUT_FILE = "output.txt"  # Output file

# Try and Catch block
try:

    # Looking for a column name from the user. Run SQLListColumns for a column list
    columnName = input('Enter a column name to sort by: ')
    outputTo = input('Output to (S)creen or (F)ile ?: ')

    if columnName is not None:

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
        cursor.execute(Commands.SELECTDATABINDCOL, (AsIs(columnName),))

        # Fetch One Row which should be the database version
        db_rows = cursor.fetchall()

        if outputTo.upper() == 'S':
            # Print Database Version / Print out the column names
            print('Database returned:')
            for row in db_rows:
                print(row)

        elif outputTo.upper() == 'F':
            # Open a file to dump data into and create a file handle
            fileDescriptor = open(OUTPUT_FILE, 'w') # Open a file for writing
            for row in db_rows:
                dataString = ','.join(str(s) for s in row)  # Take each tuple and create a string with a semicolon
                dataString = dataString.encode("ascii", "ignore") # Ignore any UTF-8 characters
                dataString = dataString.decode()    # Bring the characters back to a
                dataString = dataString + '\n'      # Add a new line to the end of a row.
                fileDescriptor.write(dataString)    # Write the first row to the file
            # Close the file handle
            fileDescriptor.close()  # Close file

        # If the connection is open, close it.
        if connection is not None:
            connection.close()
            print('Database connection closed.')
    else:
        print('Column name not given.')

except (Exception, psycopg2.DatabaseError) as error:
    print('Error: ', error)
