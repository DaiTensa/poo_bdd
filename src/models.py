from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.ext.declarative import declarative_base


# classe de base
Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    ISBN = Column(String, unique=True , primary_key=True, nullable=False, index=True)
    Book_Title = Column(String, index=True)
    Book_Author = Column(String, index=True)
    Year_Of_Publication = Column(Integer, index=True)
    Publisher = Column(String, index=True)

    def __init__(self, ISBN, Book_Title, Book_Author, Year_Of_Publication, Publisher):
        self.ISBN = ISBN 
        self.Book_Title = Book_Title
        self.Book_Author = Book_Author
        self.Year_Of_Publication = Year_Of_Publication
        self.Publisher = Publisher

    def __repr__(self):
        return f"{self.Book_Title} [{self.Book_Author}] ({self.Year_Of_Publication})"
    

class Users(Base):
    __tablename__ = "users"
    User_Id = Column(Integer, primary_key=True, unique=True, nullable=False, index=True)
    Location = Column(String, index=True)
    Age = Column(Integer, unique=False, index=True, nullable=True)

    def __init__(self, User_Id, Location, Age):
        self.User_Id = User_Id
        self.Location = Location
        self.Age = Age


class Ratings(Base):
    __tablename__ = "ratings"
    User_Id = Column(Integer, primary_key=True , index=True) #ForeignKey("users.User_Id")
    ISBN = Column(String,primary_key=True ,index=True) # ForeignKey("books.ISBN")
    Book_Rating = Column(Integer, index=True)

    def __init__(self, User_Id, ISBN, Book_Rating):
        self.User_Id = User_Id
        self.ISBN = ISBN
        self.Book_Rating = Book_Rating



