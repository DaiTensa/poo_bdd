from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import func
from statistics import mean, stdev
from sqlalchemy import select


# classe de base
Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    ISBN = Column(String, unique=True , primary_key=True, nullable=False, index=True)
    Book_Title = Column(String, index=True)
    Book_Author = Column(String,index=True)
    Year_Of_Publication = Column(Integer, index=True)
    Publisher = Column(String, index=True)

    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"{self.Book_Title} [{self.Book_Author}] ({self.Year_Of_Publication})"
    
    @classmethod
    def min_year(cls, session):
        query_years = session.query(cls.Year_Of_Publication).all()
        years = [year[0] for year in query_years if year[0] != "NULL"]
        return min(years)
    
    @classmethod
    def max_year(cls, session):
        query_years = session.query(cls.Year_Of_Publication).all()
        years = [year[0] for year in query_years if year[0] != "NULL"]
        return max(years)
    
    @classmethod
    def author_names(cls, session):
        query_author_names = session.query(cls.Book_Author).distinct().all()
        authors_names = [author[0] for author in query_author_names]
        return authors_names
    
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True ,autoincrement=True, nullable=False, index=True)
    Author_Name= Column(String, ForeignKey("books.Book_Author"),nullable=False, index=True)
    Birth_Year = Column(Integer, nullable=False, index=True)
    Death_Year = Column(Integer, index=True)
    Nationality = Column(String, nullable=False)

    books = relationship('Book')

    @classmethod
    def display_books_author(cls, session, author_name):
        stmt = select(Book.Book_Title).select_from(Book).join(Author, Author.Author_Name == Book.Book_Author).where(Author.Author_Name == author_name)
        results = session.execute(stmt)
        print(f"{author_name} books :")
        liste_books = [book[0] for book in results]
        for row in liste_books:
            print(row)
        return results

class Users(Base):
    __tablename__ = "users"
    User_Id = Column(Integer, primary_key=True, unique=True, nullable=False, index=True)
    Location = Column(String, index=True)
    Age = Column(Integer, unique=False, index=True, nullable=True)

    # moyenne des ages
    @classmethod
    def mean_ages(cls, session):
        query_ages = session.query(cls.Age).all()
        ages = [age[0] for age in query_ages if age[0] != "NULL"]
        # mean ages
        mean_age = mean(ages)
        return mean_age
    
    # ecart-type des ages
    @classmethod
    def stdev_ages(cls, session):
        query_ages = session.query(cls.Age).all()
        ages = [age[0] for age in query_ages if age[0] != "NULL"]
        # mean ages
        stdev_age = stdev(ages)
        return stdev_age
    
    # count ages
    @classmethod
    def count_ages(cls, session):
        query_ages = session.query(cls.Age).all()
        ages = [ages[0] for ages in query_ages if ages[0] != "NULL"]
        count_ages = len(ages)
        return count_ages


class Ratings(Base):
    __tablename__ = "ratings"
    User_Id = Column(Integer, primary_key=True , index=True) #ForeignKey("users.User_Id")
    ISBN = Column(String,primary_key=True ,index=True) # ForeignKey("books.ISBN")
    Book_Rating = Column(Integer, index=True)


    # moyenne des notes
    @classmethod
    def mean_ratings(cls, session):
        query_book_rating = session.query(cls.Book_Rating).all()
        ratings = [book_rating[0] for book_rating in query_book_rating if book_rating[0] != "NULL"]
        mean_rating = mean(ratings)
        return mean_rating
    
    # ecart-type des notes
    @classmethod
    def stdev_ratings(cls, session):
        query_book_rating = session.query(cls.Book_Rating).all()
        ratings = [book_rating[0] for book_rating in query_book_rating if book_rating[0] != "NULL"]
        stdev_rating = stdev(ratings)
        return stdev_rating

    # count book ratings
    @classmethod
    def count_ratings(cls, session):
        query_book_rating = session.query(cls.Book_Rating).all()
        ratings = [book_rating[0] for book_rating in query_book_rating if book_rating[0] != "NULL"]
        count_rating = len(ratings)
        return count_rating



