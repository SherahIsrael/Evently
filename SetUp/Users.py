from DBConnector import *

usersTable = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(50) NOT NULL, lastName VARCHAR(50), email VARCHAR(319) NOT NULL, dateOfBirth DATE, date DATE)"

dbcursor.execute(usersTable)

insert_users = "INSERT INTO users (firstName, lastName, email, dateOfBirth, date) VALUES (%s, %s, %s, %s, %s)"

user_values = [
    ()
]


# Insert all rows in one call
dbcursor.executemany(insert_users, user_values)  

dbcursor.execute("SHOW TABLES")

for x in dbcursor:
  print(x)