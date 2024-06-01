import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from models import Base, Book, Users, Ratings, Loan, Author


@pytest.fixture(scope='module')
def engine():
    return create_engine('sqlite:///:memory:')

@pytest.fixture(scope='module')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='module')
def session(engine,tables):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    clear_mappers()


@pytest.fixture(scope='module')
def books(session):
    book_1 = Book(ISBN="1", Book_Title="Test Book", Book_Author="Test Author", Year_Of_Publication=2020, Publisher="Test Publisher")
    book_2 = Book(ISBN="2", Book_Title="Test Book", Book_Author="Test Author", Year_Of_Publication=2020, Publisher="Test Publisher")
    session.add_all([book_1,book_2])
    session.commit()
    return [book_1,book_2]

@pytest.fixture(scope='module')
def users(session):
    user_1 = Users(User_Id=1, Location="Test Location", Age=30)
    user_2 = Users(User_Id=2, Location="Test Location", Age=30)
    user_3 = Users(User_Id=3, Location="Test Location", Age=30)
    session.add_all([user_1,user_2,user_3])
    session.commit()
    return [user_1,user_2,user_3]



@pytest.fixture(scope='module')
def ratings(session, users, books):
    rating1 = Ratings(User_Id=users[1].User_Id, ISBN=books[0].ISBN, Book_Rating=4)
    rating2 = Ratings(User_Id=users[2].User_Id, ISBN=books[1].ISBN, Book_Rating=5)
    session.add_all([rating1, rating2])
    session.commit()
    return [rating1, rating2]

def test_book_statistics(session,books):
    assert books[0].min_year(session) == 2020
    assert books[0].max_year(session) == 2020

def test_rating_statistics(session,ratings):
    assert ratings[0].mean_ratings(session) == 4.5
    assert ratings[0].stdev_ratings(session) == 0.7071067811865476