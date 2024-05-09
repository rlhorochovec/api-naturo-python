import sqlite3

# Step 1: Import the SQLite library
# Step 2: Connect to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('database/naruto.db')

# Step 3: Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 4:  Drop and Create a table called
cursor.execute("DROP TABLE IF EXISTS ninja")
cursor.execute('''CREATE TABLE IF NOT EXISTS ninja
                  (id INTEGER PRIMARY KEY, nome TEXT, categoria TEXT, vila TEXT)''')
conn.commit()

# Step 5: Insert
cursor.execute("INSERT INTO ninja (nome, categoria, vila) VALUES (?, ?, ?)", ('Naruto', 'Hokage', 'Folha'))
cursor.execute("INSERT INTO ninja (nome, categoria, vila) VALUES (?, ?, ?)", ('Gaara', 'Kazekage', 'Areia'))
conn.commit()

# Step 6: Query data from the table
cursor.execute("SELECT * FROM ninja")
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Step 7: Update
cursor.execute("UPDATE ninja SET nome = ? WHERE id = ?", ('Naruto Uzumaki', 1))
conn.commit()

# Step 8: Delete
cursor.execute("DELETE FROM ninja WHERE id = ?", (1,))
conn.commit()

# Step 9: Close the connection when you're done
conn.close()