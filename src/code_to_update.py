from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class Book(Base):
    #################
    # Modele a compléter
    pass

# Configuration de la base de données
engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def import_books_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile) # to Update???
        for row in csvreader:
            book = Book(
                ISBN=row['ISBN'],
                ###to complete
            )
            session.add(book)
        session.commit()

# Chemin vers le fichier CSV
csv_file_path = 'books.csv'
import_books_from_csv(csv_file_path)