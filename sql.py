<<<<<<< HEAD
# import sqlglot
import sqlite3
# Setup SQLite database
conn = sqlite3.connect('test.db')
=======
import sqlite3
# Setup SQLite database
conn = sqlite3.connect('test.db')

#Create a cursor object to instert record, create table, retrieve
>>>>>>> test
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
<<<<<<< HEAD
    name TEXT,
=======
    name VARCHAR(25),
    country VARCHAR(25),
>>>>>>> test
    signup_date DATE
)
''')

# Insert sample data
<<<<<<< HEAD
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Alice', '2024-08-01')")
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Bob', '2024-07-15')")
conn.commit()
=======
cursor.execute("INSERT INTO users (name, country, signup_date) VALUES ('Alice', 'India', '2024-08-01')")
cursor.execute("INSERT INTO users (name, country, signup_date) VALUES ('Bob', 'India', '2024-07-15')")
cursor.execute("INSERT INTO users (name, country, signup_date) VALUES ('Ram', 'UK', '2024-06-13')")
cursor.execute("INSERT INTO users (name, country, signup_date) VALUES ('Sham', 'USA', '2024-05-10')")
cursor.execute("INSERT INTO users (name, country, signup_date) VALUES ('Jadu', 'Canada', '2024-04-08')")

#Display the rows
data=cursor.execute("SELECT * FROM users")

for row in data:
    print(row)

conn.commit()
conn.close()
>>>>>>> test
