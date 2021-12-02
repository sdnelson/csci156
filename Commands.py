# Author: Steve Nelson
# Description: A set of commands to create database, tables and run specific commands.
# File: Commands.py
# Date: 11/23/2021
#
# Notes:
#
# Parameters:
#    None
#
# Database password
PWD = 'password'
#
# Create the database
CREATEDB = 'CREATE DATABASE netflix WITH OWNER = postgres ENCODING "UTF8" CONNECTION LIMIT = -1'

# Create the table
CREATETBL = 'CREATE TABLE IF NOT EXISTS public.shows \
( \
    show_id character varying, \
    type character varying, \
    title character varying, \
    director character varying, \
    actors character varying, \
    country character varying, \
    date_added character varying, \
    release_year character varying, \
    rating character varying, \
    duration character varying, \
    listed_in character varying, \
    description character varying \
)'
#
# Alter the table owner
ALTERTABLE = 'ALTER TABLE public.shows OWNER to postgres'
#
# List all columns only
SELECTCOLNAME = 'select column_name from information_schema.columns where table_schema = \'public\' and table_name=\'shows\''
#
# List columns and data by a specific column name
SELECTDATABINDCOL = "SELECT * FROM public.shows order by %s"
#
# List all the data from the table
SELECTALLDATA = "SELECT * FROM public.shows"
