from models import Book, Users, Ratings
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_path = 'sqlite:///data/books.db'
engine = create_engine(db_path, echo=False)

Session = sessionmaker(bind=engine)
session = Session()


# 5- Nombre de livres importés :
# rows = session.query(Book).count()
# print(f"Nombre de livres importés : {rows}")


# the_hobbit_books = select(Book.Book_Title).where(Book.Book_Title.like('%The Hobbit'))
# for title in session.scalars(the_hobbit_books):
#     print(title)

# print(Ratings.mean_ratings(session=session))
# print(Ratings.stdev_ratings(session=session))
# print(Ratings.count_ratings(session=session))


# print(Users.mean_ages(session=session))
# print(Users.stdev_ages(session=session))
# print(Users.count_ages(session=session))

print(Book.min_year(session=session))
print(Book.max_year(session=session))



