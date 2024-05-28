from faker import Faker

# initialisation faker to generate some random things
fake = Faker()

print(fake.country())

print(fake.state())



def get_user() -> str:

    return ' '.join([fake.first_name(), fake.last_name()])

