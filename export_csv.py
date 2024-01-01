import psycopg2
import csv
from io import StringIO

db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': 'postgres',
    'port': '5432'
}

def export_data():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    export_table_data(cursor, 'author', 'author.csv')
    export_table_data(cursor, 'book', 'book.csv')
    export_table_data(cursor, 'book_author', 'book_author.csv')
    export_table_data(cursor, 'book_genre', 'book_genre.csv')
    export_table_data(cursor, 'genre', 'genre.csv')

    cursor.close()
    connection.close()

def export_table_data(cursor, table_name, file_name):
    output = StringIO()
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    writer.writerow([desc[0] for desc in cursor.description])

    for row in rows:
        writer.writerow(row)

    output.seek(0)
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        file.write(output.getvalue())

if __name__ == '__main__':
    export_data()
