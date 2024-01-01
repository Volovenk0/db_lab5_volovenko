import pandas as pd
import psycopg2

db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': 'postgres',
    'port': '5432'
}

def import_data():
    rows_to_import = 50
    df = pd.read_csv('bestsellers with categories.csv', nrows=rows_to_import)

    # Введення book_id вручну
    df['book_id'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

    clear_tables()

    insert_books(df)

def clear_tables():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM book_genre;")
    cursor.execute("DELETE FROM book_author;")

    cursor.execute("DELETE FROM book;")

    connection.commit()

    cursor.close()
    connection.close()

def insert_books(df):
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    for index, row in df.iterrows():
        book_id = row['book_id']  # Змінено для використання введеного book_id

        cursor.execute("""
            INSERT INTO book (book_id, book_name, price, rating)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (book_id, row['Name'], row['Price'], row['User Rating']))


    connection.commit()

    cursor.close()
    connection.close()

if __name__ == '__main__':
    import_data()
