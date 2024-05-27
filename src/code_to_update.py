import sys
sys.path.append('/home/dai/Documents/Python_Projects/sql/sqlite_projects')


from sqlalchemy import create_engine
from models import Base
from utils.mes_fonctions import import_books_from_csv 
from sqlalchemy.orm import sessionmaker
from models import Book



db_path = 'sqlite:///books.db'


# Configuration de la base de données
engine = create_engine(db_path)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Chemin vers le fichier CSV
csv_file_path = '/home/dai/Documents/Python_Projects/sql/sqlite_projects/data/books.csv'
import_books_from_csv(csv_file_path, session= session, model=Book)