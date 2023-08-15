import sqlite3

# Connecting to the MLS (Major League Soccer) Database
connection_object = sqlite3.connect("Major_League_Soccer.db")

# Creating cursor object to be able to execute and play with the queries in the database
curser_object = connection_object.cursor()

