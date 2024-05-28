import sys
sys.path.append('/home/dai/Documents/Python_Projects/sql/sqlite_projects')


from sqlalchemy import create_engine
from models import Base
from utils.mes_fonctions import import_books_from_csv 
from sqlalchemy.orm import sessionmaker
from models import Book
from sqlalchemy import select



db_path = 'sqlite:///data/books.db'


# Configuration de la base de données
engine = create_engine(db_path)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Chemin vers le fichier CSV
# Modification de l'affichage d'un livre avec la méthode __repr__
csv_file_path = '/home/dai/Documents/Python_Projects/sql/sqlite_projects/data/books.csv'
import_books_from_csv(csv_file_path, session= session, model=Book)

# 5- Nombre de livres importés :
rows = session.query(Book).count()
print(f"Nombre de livres importés : {rows}")

the_hobbit_books = select(Book.Book_Title).where(Book.Book_Title.like('%The Hobbit'))
for title in session.scalars(the_hobbit_books):
    print(title)