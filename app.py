from pymongo import MongoClient
from faker import Faker
from datetime import datetime
import csv

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    #CONNECTION_STRING = "mongodb+srv://grupoDinamita:GrupoDinamita3@lab03.sutnr1c.mongodb.net/"
    CONNECTION_STRING = "mongodb://localhost:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial)
    return client['Lab03']

def insert_random_books(collection):
    fake = Faker()
    books_data = []
    for _ in range(10):  # Inserting 10 random books as an example
        book = {
            "title": fake.catch_phrase(),
            "author": fake.name(),
            "genre": fake.word(),
            "publication_year": fake.year(),
            "publisher": fake.company(),
            "pages": fake.random_number(digits=3),
            "price": fake.random_number(digits=2),
            "sales": fake.random_number(digits=4),
            "user_rating": round(fake.random.uniform(1, 5), 1),
            "availability": fake.random_number(digits=2)
        }
        collection.insert_one(book)
        books_data.append(book)
    return books_data

def insert_random_authors(collection):
    fake = Faker()
    authors_data = []
    for _ in range(5):  # Inserting 5 random authors as an example
        author = {
            "name": fake.name(),
            "id": fake.uuid4(),
            "num_publications": fake.random_number(digits=2),
            "age": fake.random_int(min=18, max=90),
            "gender": fake.random_element(elements=("Male", "Female")),
            "email": fake.email(),
            "country": fake.country()
        }
        collection.insert_one(author)
        authors_data.append(author)
    return authors_data

def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

if __name__ == "__main__":
    # Get the database
    dbname = get_database()

    # Insert random books
    books_collection = dbname["books"]
    books_data = insert_random_books(books_collection)
    export_to_csv(books_data, 'books_data.csv')

    # Insert random authors
    authors_collection = dbname["authors"]
    authors_data = insert_random_authors(authors_collection)
    export_to_csv(authors_data, 'authors_data.csv')

    print("Data insertion completed.")