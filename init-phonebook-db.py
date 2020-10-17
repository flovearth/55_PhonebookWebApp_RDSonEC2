import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'admin',
  'password': 'clarusway-1',
  'host': 'phonebook-app-db.cbanmzptkrzf.us-east-1.rds.amazonaws.com',
  'database': 'phonebook',
  'raise_on_warnings': True
}

# Write a function named `init_phonebook_db` which initializes the phonebook db
# Create phonebook table within mysql db and populate with sample data
def init_phonebook_db(cursor):
    drop_table = 'DROP TABLE IF EXISTS phonebook.phonebook;'
    phonebook_table = """
    CREATE TABLE phonebook(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    number VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """
    data = """
    INSERT INTO phonebook.phonebook (name, number)
    VALUES
        ("Callahan", "1234567890"),
        ("Sergio Taco", "67854"),
        ("Vincenzo Altobelli", "876543554");
    """
    #cursor.execute(drop_table)
    cursor.execute(phonebook_table)
    cursor.execute(data)

try:
  cnx = mysql.connector.connect(**config)
  init_phonebook_db(cnx.cursor(buffered=True))
  cnx.commit()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("Phonebook table created and populated with successfully")
  cnx.close()