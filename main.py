import psycopg2
import matplotlib.pyplot as plt


db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': 'postgres',
    'port': '5432'
}

# Запит 1: Створення зрізу для першого запиту
create_view_1 = '''
create or replace view max_ratings_by_genre as
select max(book.rating) as max_rating, genre.genre_name 
	from book join book_genre
		on book.book_id = book_genre.book_id
			join genre
				on book_genre.genre_id = genre.genre_id
group by genre.genre_name
order by max_rating desc;
'''

# Запит 2: Створення зрізу для другого запиту
create_view_2 = '''
create or replace view top_authors_by_rating as
select author.author_name, max(book.rating) as max_rating
	from author join book_author
		on author.author_id = book_author.author_id
			join book
				on book_author.book_id = book.book_id
group by author.author_name
order by max_rating desc
limit 5;
'''

# Запит 3: Створення зрізу для третього запиту
create_view_3 = '''
create or replace view book_counts_by_genre as
select genre.genre_name, count(book.book_id) as book_count
	from book join book_genre
		on book.book_id = book_genre.book_id
			join genre
				on book_genre.genre_id = genre.genre_id
where book.price < 12
group by genre.genre_name
order by book_count desc;
'''

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall() if cursor.description else None

def plot_bar_chart(ax, labels, values, xlabel, ylabel, title):
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum', 'lightpink', 'bisque', 'lightsteelblue', 'mediumaquamarine', 'salmon']
    ax.bar(labels, values, color=colors)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

def plot_pie_chart(ax, labels, sizes, title):
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'plum']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    ax.set_title(title)

def plot_line_chart(ax, x, y, xlabel, ylabel, title):
    ax.plot(x, y, marker='o', color='orchid')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha='right')

def main():
    connection = psycopg2.connect(
        user=db_params['user'],
        password=db_params['password'],
        dbname=db_params['database'],
        host=db_params['host'],
        port=db_params['port']
    )

    with connection.cursor() as cursor:
        # Створення зрізів
        execute_query(cursor, create_view_1)
        execute_query(cursor, create_view_2)
        execute_query(cursor, create_view_3)

        # Запит 1: Візуалізація – стовпчикова діаграма
        result_1 = execute_query(cursor, 'select * from max_ratings_by_genre;')
        if result_1 is not None:
            genres = [row[1] for row in result_1]
            ratings = [row[0] for row in result_1]

        # Запит 2: Візуалізація – кругова діаграма
        result_2 = execute_query(cursor, 'select * from top_authors_by_rating;')
        if result_2 is not None:
            authors = [row[0] for row in result_2]
            ratings_authors = [row[1] for row in result_2]

        # Запит 3: Візуалізація – графік залежності
        result_3 = execute_query(cursor, 'select * from book_counts_by_genre;')
        if result_3 is not None:
            genres_prices = [row[0] for row in result_3]
            book_counts = [row[1] for row in result_3]

        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        if result_1 is not None:
            plot_bar_chart(axs[0], genres, ratings, 'Genre', 'Rating', 'Book Ratings by Genre')
        if result_2 is not None:
            plot_pie_chart(axs[1], authors, ratings_authors, 'Top 5 Authors by Book Rating')
        if result_3 is not None:
            plot_line_chart(axs[2], genres_prices, book_counts, 'Genre', 'Book Count', 'Book Counts by Genre (Price < $12)')

        plt.subplots_adjust(wspace=0.5)
        plt.show()

if __name__ == '__main__':
    main()
