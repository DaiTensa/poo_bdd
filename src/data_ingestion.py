import sys
sys.path.append('/home/dai/Documents/Python_Projects/sql/sqlite_projects')


from sqlalchemy import create_engine
from models import Base
from utils.mes_fonctions import import_books_from_csv, import_users_from_csv, import_ratings_from_csv, fake_authors_populate
from sqlalchemy.orm import sessionmaker
from models import Book, Users, Ratings, Author, Loan

db_path = 'sqlite:///data/books.db'


# Configuration de la base de données
engine = create_engine(db_path)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

    # Import Books
    csv_file_path_books = '/home/dai/Documents/Python_Projects/sql/sqlite_projects/data/books.csv'
    import_books_from_csv(csv_file_path_books, session= session, model=Book)


    # Import Users
    csv_file_path_users = '/home/dai/Documents/Python_Projects/sql/sqlite_projects/data/users.csv'
    import_users_from_csv(csv_file_path_users, session= session, model=Users)


    # Import Ratings
    csv_file_path_ratings = '/home/dai/Documents/Python_Projects/sql/sqlite_projects/data/ratings.csv'
    import_ratings_from_csv(csv_file_path_ratings, session= session, model=Ratings)


    liste_authors = Book.author_names(session=session)
    fake_authors_populate(liste_author_names = liste_authors, model =Author, session=session)


