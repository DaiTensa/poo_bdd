import sys
sys.path.append('/home/dai/Documents/Python_Projects/sql/sqlite_projects')

from models import Book, Users, Ratings, Author, Loan
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.mes_fonctions import fake_authors_populate

# engine maker
db_path = 'sqlite:///data/books.db'
engine = create_engine(db_path, echo=False)

# session maker
Session = sessionmaker(bind=engine)
session = Session()


# count books imported
# rows = session.query(Book).count()
# print(f"Nombre de livres importés : {rows}")


# # hobbit books
# the_hobbit_books = select(Book.Book_Title).where(Book.Book_Title.like('%The Hobbit'))
# for title in session.scalars(the_hobbit_books):
#     print(title)


# # mean stdev count Ratings
# print(Ratings.mean_ratings(session=session))
# print(Ratings.stdev_ratings(session=session))
# print(Ratings.count_ratings(session=session))


# # mean stdev count Users
# print(Users.mean_ages(session=session))
# print(Users.stdev_ages(session=session))
# print(Users.count_ages(session=session))


# # min max year book 
# print(Book.min_year(session=session))
# print(Book.max_year(session=session))



# display athor book ex : David Benioff
David_Benioff_books = Author.display_books_author(session=session, author_name= "David Benioff")


# display athor book  ex: Carlo D'Este
Carlo_D_Este_books = Author.display_books_author(session=session, author_name= "Carlo D'Este")


# # Ajout d'un prêt - simulation 
Loan.add_loan(user_id=2, book_ref= "0195153448", session=session)
Loan.add_loan(user_id=2, book_ref= "0679425608", session=session)
Loan.add_loan(user_id=3, book_ref= "080652121X", session=session)
Loan.add_loan(user_id=3, book_ref= "055321215X", session=session)
Loan.add_loan(user_id=10, book_ref= "0340767936", session=session)
Loan.add_loan(user_id=11, book_ref= "0340767936", session=session)

# # Retourner un prêt simulation
Loan.return_laon(user_id=11, book_ref= "0340767936", session=session)
