import mysql.connector

# Database connection configuration
config = {
    'user': 'seshuvarma',
    'password': 'Password@1',
    'host': 'localhost',
    'database': 'booklibrary'
}

def connect_db():
    return mysql.connector.connect(**config)

# Function to select a book by title
def select_book_by_title(title):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM books WHERE title = %s"
    cursor.execute(query, (title,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return book

# Function to update the author of a book
def update_book_author(title, new_author):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE books SET author = %s WHERE title = %s"
    cursor.execute(query, (new_author, title))
    conn.commit()
    cursor.close()
    conn.close()

# Function to delete a book by title
def delete_book_by_title(title):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM books WHERE title = %s"
    cursor.execute(query, (title,))
    conn.commit()
    cursor.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    # Insert example data
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            year INT NOT NULL
        )
    """)
    books_data = [
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
        ('To Kill a Mockingbird', 'Harper Lee', 1960),
        ('1984', 'George Orwell', 1949)
    ]
    cursor.executemany("""
        INSERT INTO books (title, author, year)
        VALUES (%s, %s, %s)
    """, books_data)
    conn.commit()
    cursor.close()
    conn.close()

    # Select a book by title
    book = select_book_by_title('1984')
    print(f"Selected book: {book}")

    # Update the author of a book
    update_book_author('1984', 'Eric Arthur Blair')
    print("Updated author of '1984'")

    # Verify the update
    updated_book = select_book_by_title('1984')
    print(f"Updated book: {updated_book}")

    # Delete a book by title
    delete_book_by_title('The Great Gatsby')
    print("Deleted 'The Great Gatsby'")

    # Verify the deletion
    deleted_book = select_book_by_title('The Great Gatsby')
    print(f"Deleted book: {deleted_book}")

