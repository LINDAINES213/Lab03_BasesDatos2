from pymongo import MongoClient
from faker import Faker
from datetime import datetime

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

def insert_random_authors(collection):
    fake = Faker()
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

if __name__ == "__main__":
    # Get the database
    dbname = get_database()

    # Insert random books
    books_collection = dbname["books"]
    insert_random_books(books_collection)

    # Insert random authors
    authors_collection = dbname["authors"]
    insert_random_authors(authors_collection)

    print("Data insertion completed.")