from config import *

# Establish a new database connection
import mysql.connector;

mydb = mysql.connector.connect(
  host="localhost",
  user= DBuser,
  password= DBpassword,
  database=myDatabase
)

# Use database connection
dbcursor = mydb.cursor()

