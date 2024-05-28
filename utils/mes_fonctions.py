import csv

def import_books_from_csv(csv_file_path, session, model):
    with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        number_of_rows = 0

        for row in csvreader:
            if number_of_rows >=29:
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

