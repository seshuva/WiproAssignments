import mysql.connector

# Database connection configuration
config = {
    'user': 'seshuvarma',
    'password': 'Password@1',
    'host': 'localhost',
    'database': 'booklibrary'
}

# Establish a database connection
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Create the books table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        year INT NOT NULL
    )
""")

# Insert multiple rows into the books table
books_data = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
    ('To Kill a Mockingbird', 'Harper Lee', 1960),
    ('1984', 'George Orwell', 1949)
]

cursor.executemany("""
    INSERT INTO books (title, author, year)
    VALUES (%s, %s, %s)
""", books_data)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Books table created and data inserted successfully.")
