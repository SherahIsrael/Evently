from DBConnector import *

dbcursor.execute("DROP TABLE IF EXISTS registrationTable")

registrationTable = "CREATE TABLE IF NOT EXISTS registration (registrationId INT AUTO_INCREMENT PRIMARY KEY, Person INT, time TIME, Event INT FOREIGN KEY (Event) REFERENCES Events(eventId), FOREIGN KEY (Person) REFERENCES Users(userId))"
# firstName VARCHAR(50) NOT NULL, email VARCHAR(150) NOT NULL, eventDate DATE


dbcursor.execute(registrationTable)

# dbcursor.execute("SELECT Concat(firstName, ' ' , email) AS fullName FROM Users")
  
# dbcursor.execute("SELECT * FROM registrationTable") 

# # fetch all the matching rows  
# registrationResult = dbcursor.fetchall() 
  
# # loop through the rows 
# for row in registrationResult: 
#     print(row) 
#     print("\n") 


