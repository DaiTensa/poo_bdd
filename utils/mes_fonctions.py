import csv

from faker import Faker

# initialisation faker to generate some random things
fake = Faker()


# function to import books
def import_books_from_csv(csv_file_path, session, model):
    with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        number_of_rows = 0

        for row in csvreader:
            if number_of_rows >=50000:
                break
            book = model(
                ISBN=row['ISBN'],
                Book_Title=row['Book-Title'],
                Book_Author=row['Book-Author'],
                Year_Of_Publication= int(row['Year-Of-Publication']),
                Publisher=row['Publisher']
            )
            session.add(book)
            print(book)
            number_of_rows += 1
        session.commit()

# function to import users data
def import_users_from_csv(csv_file_path, session, model):
    with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        number_of_rows = 0
    
        for row in csvreader:
            if number_of_rows >=50000:
                break
            user = model(
                User_Id=row['User-ID'],
                Location=row['Location'],
                Age=row['Age']
            )
            session.add(user)
            number_of_rows += 1
        session.commit()

# function to import books ratings
def import_ratings_from_csv(csv_file_path, session, model):
    with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        number_of_rows = 0

        for row in csvreader:
            if number_of_rows >=50000:
                break
            rating = model(
                User_Id=row['User-ID'],
                ISBN=row['ISBN'],
                Book_Rating=row['Book-Rating']
            )
            session.add(rating)
            # print(rating)
            number_of_rows += 1
        session.commit()


# data authors tables
def fake_authors_populate(liste_author_names, model, session):
    for author_name in liste_author_names:
        birth_year = fake.year()
        death_year = int(birth_year) + 50
        author = model(
            Author_Name = author_name,
            Birth_Year = birth_year,
            Death_Year = death_year,
            Nationality = fake.country()
        )
        session.add(author)
    session.commit()