from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.ext.declarative import declarative_base


# classe de base
Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    
    ISBN = Column(String, primary_key=True, index=True)
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
        return f"{self.Book_Title}[{self.Book_Author}]({self.Year_Of_Publication})"

