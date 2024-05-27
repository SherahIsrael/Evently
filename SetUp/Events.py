from DBConnector import *

eventsTable = "CREATE TABLE IF NOT EXISTS events (id INT AUTO_INCREMENT PRIMARY KEY, eventName VARCHAR(50) NOT NULL, date DATE NOT NULL, StartTime TIME(0) NOT NULL, EndTime TIME(0) NOT NULL, capacity SMALLINT(250))"

dbcursor.execute(eventsTable)







dbcursor.execute("SHOW TABLES")

for x in dbcursor:
  print(x)