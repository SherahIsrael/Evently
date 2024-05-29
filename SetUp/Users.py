from DBConnector import *

dbcursor.execute("DROP TABLE IF EXISTS users")

usersTable = "CREATE TABLE IF NOT EXISTS users (userId INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(50) NOT NULL, lastName VARCHAR(50), email VARCHAR(150) NOT NULL, dateOfBirth DATE, registrationDate DATE)"

dbcursor.execute(usersTable)

insert_users = "INSERT INTO users (firstName, lastName, email, dateOfBirth, registrationDate) VALUES (%s, %s, %s, %s, %s)"

user_values = [
  ('Juan', 'Rodriguez', 'juan.rodriguez@example.com', '1990-03-15', '2024-04-15'),
  ('Maria', 'Gonzalez', 'maria.gonzalez@example.com', '1985-07-22', '2024-05-10'),
  ('José', 'Martinez', 'jose.martinez@example.com', '1978-11-30', '2024-06-12'),
  ('Ana', 'Fernandez', 'ana.fernandez@example.com', '1982-01-14', '2024-07-19'),
  ('Luis', 'Hernandez', 'luis.hernandez@example.com', '1993-05-24', '2024-08-02'),
  ('Carlos', 'Lopez', 'carlos.lopez@example.com', '1976-09-05', '2024-09-20'),
  ('Patricia', 'Garcia', 'patricia.garcia@example.com', '1997-12-17', '2024-10-01'),
  ('Angela', 'Wilson', 'angela.wilson@example.com', '2002-06-03', '2024-04-20'),
  ('Aisha', 'Mohamed', 'aisha.mohamed@example.com', '1995-04-10', '2024-05-15'),
  ('Kwame', 'Mensah', 'kwame.mensah@example.com', '1988-10-22', '2024-06-05'),
  ('Ama', 'Boateng', 'ama.boateng@example.com', '1990-08-17', '2024-07-13'),
  ('Sofia', 'Ramos', 'sofia.ramos@example.com', '1996-11-29', '2024-08-22'),
  ('Mateo', 'Cruz', 'mateo.cruz@example.com', '1981-02-26', '2024-09-07'),
  ('Lucas', 'Vargas', 'lucas.vargas@example.com', '1975-07-08', '2024-04-25'),
  ('Miguel', 'Jimenez', 'miguel.jimenez@example.com', '1983-03-18', '2024-05-28'),
  ('Camila', 'Torres', 'camila.torres@example.com', '2003-12-05', '2024-06-21'),
  ('Gabriel', 'Alvarez', 'gabriel.alvarez@example.com', '1977-09-14', '2024-07-30'),
  ('Rosa', 'Gomez', 'rosa.gomez@example.com', '1984-05-11', '2024-08-14'),
  ('Samuel', 'Pereira', 'samuel.pereira@example.com', '1992-10-01', '2024-09-26'),
  ('Isabella', 'Castro', 'isabella.castro@example.com', '1999-02-08', '2024-04-12'),
  ('Diego', 'Flores', 'diego.flores@example.com', '1989-03-25', '2024-05-06'),
  ('Esteban', 'Silva', 'esteban.silva@example.com', '1986-07-16', '2024-06-30'),
  ('Bruna', 'Moura', 'bruna.moura@example.com', '1974-01-03', '2024-08-05'),
  ('Daniel', 'Bello', 'daniel.bello@example.com', '2000-12-27', '2024-09-10'),
  ('Helena', 'Teixeira', 'helena.teixeira@example.com', '1994-09-21', '2024-05-21'),
  ('Thiago', 'Fernandes', 'thiago.fernandes@example.com', '1979-06-14', '2024-07-07'),
  ('Kofi', 'Adjei', 'kofi.adjei@example.com', '1987-04-08', '2024-09-19'),
  ('Yemi', 'Oladele', 'yemi.oladele@example.com', '1991-08-20', '2024-04-09'),
  ('Chinwe', 'Okoro', 'chinwe.okoro@example.com', '1973-02-14', '2024-06-18'),
  ('Femi', 'Adebayo', 'femi.adebayo@example.com', '2005-03-01', '2024-08-31'),
  ('Laurel', 'Lindenbluth', 'llindenbluth1@google.es', '1994-03-07', '2023-08-23'),
  ('Patrizius', 'Geator', 'pgeator0@narod.ru', '1989-12-01', '2023-06-18'),
  ('Lydon', 'Pierce', 'lpierce2@weebly.com', '2005-02-05', '2024-10-16'),
  ('Ansell', 'Radmer', 'aradmer3@bbc.co.uk', '1982-10-12', '2024-02-25'),
  ('Benetta', 'Riatt', 'briatt4@pcworld.com', '1983-01-26', '2024-03-03'),
  ('Giusto', 'Brickdale', 'gbrickdale5@1und1.de', '2001-01-20', '2024-08-29'),
  ('Katuscha', 'Leffek', 'kleffek6@guardian.co.uk', '1992-06-07', '2024-09-20'),
  ('Gert', 'Fredi', 'gfredi7@parallels.com', '1975-10-11', '2024-08-03'),
  ('Arnuad', 'Calf', 'acalf8@hostgator.com', '1979-09-06', '2023-06-24'),
  ('Salvatore', 'Fidgin', 'sfidgin9@jugem.jp', '1998-05-17', '2024-05-08'),
  ('Jabez', 'Bower', 'jbowera@trellian.com', '1980-05-26', '2023-07-11'),
  ('Dmitri', 'Ruger', 'drugerb@mtv.com', '1976-02-07', '2023-09-13'),
  ('Cindy', 'Stodhart', 'cstodhartc@usnews.com', '1993-07-09', '2024-04-23'),
  ('Maxie', 'Spir', 'mspird@java.com', '2005-04-19', '2024-04-12'),
  ('Celeste', 'Galliard', 'cgalliarde@fastcompany.com', '1973-08-27', '2024-07-10'),
  ('Averill', 'MacCallester', 'amaccallesterf@weebly.com', '1994-08-10', '2024-02-06'),
  ('Nichole', 'Albion', 'nalbiong@bigcartel.com', '1987-06-02', '2023-07-28'),
  ('Irwin', 'Kilfoyle', 'ikilfoyleh@github.io', '1975-06-09', '2024-01-01'),
  ('Gun', 'Kuhlen', 'gkuhleni@admin.ch', '1975-03-06', '2023-05-08'),
  ('Webb', 'Chidlow', 'wchidlowj@nydailynews.com', '1975-03-15', '2024-05-28'),
  ('Katina', 'Fortnam', 'kfortnamk@google.com', '2003-01-03', '2024-01-18'),
  ('Stephie', 'Crace', 'scracel@cdbaby.com', '2001-10-18', '2023-08-20'),
  ('Erasmus', 'Taunton.', 'etauntonm@lulu.com', '1990-12-23', '2023-05-08'),
  ('Maxi', 'Ioselevich', 'mioselevichn@tamu.edu', '1992-02-02', '2024-10-31'),
  ('Malcolm', 'Reames', 'mreameso@plala.or.jp', '1992-12-25', '2023-04-27'),
  ('Karly', 'Gofton', 'kgoftonp@google.ru', '1991-06-26', '2023-12-09'),
  ('Simone', 'Smales', 'ssmalesq@cbslocal.com', '1979-04-21', '2024-02-28'),
  ('Nonie', 'Moggle', 'nmoggler@ovh.net', '1993-09-22', '2024-03-10'),
  ('Ida', 'MacAnulty', 'imacanultys@kickstarter.com', '1995-04-08', '2024-08-03'),
  ('Wandis', 'Gundrey', 'wgundreyt@bloomberg.com', '1989-07-18', '2024-09-04'),
  ('Verna', 'Laurant', 'vlaurantu@umich.edu', '1996-12-24', '2023-12-05'),
  ('Brooks', 'Corah', 'bcorahv@cmu.edu', '1978-05-31', '2024-10-05'),
  ('Willis', 'Purton', 'wpurtonw@dyndns.org', '1999-09-22', '2024-10-04'),
  ('Falito', 'Cowgill', 'fcowgillx@mit.edu', '1992-11-28', '2023-09-11'),
  ('Abagael', 'Blampy', 'ablampyy@wikipedia.org', '1978-03-16', '2023-08-07'),
  ('Scotty', 'Leverington', 'sleveringtonz@independent.co.uk', '1996-05-08', '2024-09-23'),
  ('Rosanna', 'Samme', 'rsamme10@cnet.com', '1997-11-10', '2024-03-17'),
  ('Karna', 'Stonuary', 'kstonuary11@twitter.com', '1994-05-11', '2023-05-01'),
  ('Alexi', 'Bootell', 'abootell12@uol.com.br', '2002-09-26', '2024-09-04'),
  ('Wiatt', 'Codlin', 'wcodlin13@bing.com', '1998-11-22', '2023-07-31')
]

# Insert all rows in one call
dbcursor.executemany(insert_users, user_values)  

mydb.commit()

dbcursor.execute("SELECT * FROM users") 
  
# fetch all the matching rows  
result = dbcursor.fetchall() 
  
# loop through the rows 
for row in result: 
    print(row) 
    print("\n") 

mydb.close()