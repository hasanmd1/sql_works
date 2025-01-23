import random
from faker import Faker

fake = Faker()

def generate_users(n):
    users = []
    for _ in range(n):
        name = fake.name().replace('\'', '')
        email = fake.email().replace('\'', '')
        phone = fake.phone_number().replace('\'', '').replace('x', '').replace('X', '').replace('(', '').replace(')', '').replace('-', '')
        address = fake.address().replace('\n', ', ').replace('\'', '')
        users.append((name, email, phone, address))
    return users

def generate_authors(n, user_ids):
    authors = []
    for user_id in user_ids:
        name = fake.name().replace('\'', '')
        biography = fake.text().replace('\'', '')
        nationality = fake.country().replace('\'', '')
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
        death_date = fake.date_of_birth(minimum_age=0, maximum_age=17) if random.choice([True, False]) else None
        authors.append((user_id, name, biography, nationality, birth_date, death_date))
    return authors

def generate_genres(n):
    genres = []
    genre_names = set()
    while len(genres) < n:
        name = fake.word().capitalize().replace('\'', '')
        if name not in genre_names:
            genre_names.add(name)
            description = fake.text().replace('\'', '')
            genres.append((name, description))
    return genres

def generate_books(n):
    books = []
    for _ in range(n):
        title = fake.sentence(nb_words=4)
        publication_year = random.randint(1900, 2023)
        isbn = fake.isbn13().replace('-', '')
        pages = random.randint(100, 1000)
        language = fake.language_name().replace('\'', '')
        publisher = fake.company().replace('\'', '')
        books.append((title, publication_year, isbn, pages, language, publisher))
    return books

def generate_book_authors(n, book_ids, author_ids):
    book_authors = []
    for _ in range(n):
        book_id = random.choice(book_ids)
        author_id = random.choice(author_ids)
        contribution = fake.job().replace('\'', '')
        book_authors.append((book_id, author_id, contribution))
    return book_authors

def generate_book_genres(n, book_ids, genre_ids):
    book_genres = []
    for _ in range(n):
        book_id = random.choice(book_ids)
        genre_id = random.choice(genre_ids)
        book_genres.append((book_id, genre_id))
    return book_genres

def generate_book_copies(n, book_ids):
    book_copies = []
    for _ in range(n):
        book_id = random.choice(book_ids)
        status = random.choice(['available', 'checked out', 'reserved'])
        condition = fake.word().replace('\'', '')
        acquisition_date = fake.date()
        location = fake.address().replace('\n', ', ')
        book_copies.append((book_id, status, condition, acquisition_date, location))
    return book_copies

def generate_reservations(n, user_ids, copy_ids):
    reservations = []
    for _ in range(n):
        user_id = random.choice(user_ids)
        copy_id = random.choice(copy_ids)
        reservation_date = fake.date_time_this_year()
        due_date = fake.date_between(start_date=reservation_date, end_date='+30d')
        return_date = fake.date_time_between(start_date=reservation_date, end_date=due_date) if random.choice([True, False]) else None
        status = random.choice(['reserved', 'returned', 'overdue'])
        reservations.append((user_id, copy_id, reservation_date, due_date, return_date, status))
    return reservations

def write_sample_data(users, authors, genres, books, book_authors, book_genres, book_copies, reservations):
    with open('sample_data.sql', 'w') as f:
        f.write('-- Sample Data for MySQL Schema\n\n')
        
        f.write('-- Insert sample data into users table\n')
        f.write('INSERT INTO library.users (name, email, phone, address) VALUES\n')
        f.write(',\n'.join([f"('{name}', '{email}', '{phone}', '{address}')" for name, email, phone, address in users]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into authors table\n')
        f.write('INSERT INTO library.authors (user_id, name, biography, nationality, birth_date, death_date) VALUES\n')
        f.write(',\n'.join([f"({user_id}, '{name}', '{biography}', '{nationality}', '{birth_date}', {f'\'{death_date}\'' if death_date else 'NULL'})" for user_id, name, biography, nationality, birth_date, death_date in authors]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into genres table\n')
        f.write('INSERT INTO library.genres (name, description) VALUES\n')
        f.write(',\n'.join([f"('{name}', '{description}')" for name, description in genres]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into books table\n')
        f.write('INSERT INTO library.books (title, publication_year, isbn, pages, language, publisher) VALUES\n')
        f.write(',\n'.join([f"('{title}', {publication_year}, '{isbn}', {pages}, '{language}', '{publisher}')" for title, publication_year, isbn, pages, language, publisher in books]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into book_authors table\n')
        f.write('INSERT INTO library.book_authors (book_id, author_id, contribution) VALUES\n')
        f.write(',\n'.join([f"({book_id}, {author_id}, '{contribution}')" for book_id, author_id, contribution in book_authors]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into book_genres table\n')
        f.write('INSERT INTO library.book_genres (book_id, genre_id) VALUES\n')
        f.write(',\n'.join([f"({book_id}, {genre_id})" for book_id, genre_id in book_genres]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into book_copies table\n')
        f.write('INSERT INTO library.book_copies (book_id, status, condition, acquisition_date, location) VALUES\n')
        f.write(',\n'.join([f"({book_id}, '{status}', '{condition}', '{acquisition_date}', '{location}')" for book_id, status, condition, acquisition_date, location in book_copies]))
        f.write(';\n\n')
        
        f.write('-- Insert sample data into reservations table\n')
        f.write('INSERT INTO library.reservations (user_id, copy_id, reservation_date, due_date, return_date, status) VALUES\n')
        f.write(',\n'.join([f"({user_id}, {copy_id}, '{reservation_date}', '{due_date}', {f'\'{return_date}\'' if return_date else 'NULL'}, '{status}')" for user_id, copy_id, reservation_date, due_date, return_date, status in reservations]))
        f.write(';\n')

if __name__ == '__main__':
    num_entries = 100 # we want 100 entries for each table
    users = generate_users(num_entries)
    user_ids = list(range(1, num_entries + 1))
    authors = generate_authors(num_entries, user_ids)
    genres = generate_genres(num_entries)
    genre_ids = list(range(1, num_entries + 1))
    books = generate_books(num_entries)
    book_ids = list(range(1, num_entries + 1))
    book_authors = generate_book_authors(num_entries, book_ids, user_ids)
    book_genres = generate_book_genres(num_entries, book_ids, genre_ids)
    book_copies = generate_book_copies(num_entries, book_ids)
    copy_ids = list(range(1, num_entries + 1))
    reservations = generate_reservations(num_entries, user_ids, copy_ids)
    
    write_sample_data(users, authors, genres, books, book_authors, book_genres, book_copies, reservations)