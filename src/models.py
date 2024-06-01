from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import func
from statistics import mean, stdev
from sqlalchemy import select
from datetime import date


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

    def display_books_author(session, author_name):
        stmt = select(Book.Book_Title).select_from(Book).join(Author, Author.Author_Name == Book.Book_Author).where(Author.Author_Name == author_name)
        results = session.execute(stmt)
        print(f"{author_name} books :")
        liste_books = [book[0] for book in results]
        for row in liste_books:
            print(row)
        print()
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


#1- création d'un prêt --> id auto incrémenté (on fait un prêt si book_ref in Book_ISBN et Si Status = "Rendu")
#2- référence à un livre et un user :
    # livre : si disponible (book_ref in Book_Ref and Loan_Status = "Rendu")
    # user : pas plus de 5 prêts (en cours)
    # date de début : date de création du prêt
#3- une méthode : retourner un prêt
    # status : en cours à rendu
    # la date se met à jour
    # le livre devient disponible
    # user un prêt en moins

class Loan(Base):
    __tablename__ = "loans"
    Id = Column(Integer, primary_key=True ,autoincrement=True, index=True, nullable=False)
    User_Id = Column(Integer, ForeignKey("users.User_Id"),index=True)
    Book_Ref = Column(String, ForeignKey("books.ISBN"),nullable=False, index=True)
    Laon_Date = Column(Date, default=date.today())
    Laon_End_Date = Column(Date, nullable=True)
    Loan_Status = Column(String)

    user = relationship("Users")
    book = relationship("Book")

    @classmethod
    def add_loan(cls, user_id, book_ref, session):

        # Si le livre existe dans la base de données
        # query_all_books_isbn = session.query(Book.ISBN).all()
        # liste_isbn = [isbn[0] for isbn in query_all_books_isbn]
        # if not book_ref  in liste_isbn:
        #     print(f"Le livre {book_ref} n'existe pas !")
        #     return

        # 1- Vérifier si le livre est disponible
        book = session.query(cls).filter_by(Book_Ref=book_ref, Loan_Status = "Rendu")
        if not book:
            print(f"Le livre n'est pas disponible aujourd'huit - {date.today()}")
            return
        
        # 2- pas plus de 5 livres
        pret_actif_count = session.query(cls).filter_by(User_Id = user_id, Loan_Status = "En cours").count()
        if pret_actif_count >= 5:
            print(f"{user_id} {date.today()} vous avez {pret_actif_count} prêts en cours !")
            return
        
        # 3- Création du pret
        pret = cls(
        User_Id = user_id,
        Book_Ref = book_ref,
        Laon_Date = date.today(),
        Loan_Status = "En cours"
    )
        session.add(pret)
        session.commit()
        print(f"{user_id} pret crée avec succès !")
        return pret

    @classmethod
    def return_laon(cls):
        pass

