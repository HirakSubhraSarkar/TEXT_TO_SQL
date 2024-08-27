import sqlite3
# Setup SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    signup_date DATE
)
''')

# Insert sample data
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Alice', '2024-08-01')")
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Bob', '2024-07-15')")
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Ram', '2024-06-13')")
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Sham', '2024-05-10')")
cursor.execute("INSERT INTO users (name, signup_date) VALUES ('Jadu', '2024-04-08')")

conn.commit()
