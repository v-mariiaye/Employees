import csv
import random
from faker import Faker
from middle_names import ukrainian_middle_names

fake = Faker('uk_UA')


def generate_employee():
    first_name = fake.first_name()
    last_name = fake.last_name()
    middle_name = random.choice(ukrainian_middle_names)
    gender = random.choice(['Жінка', 'Чоловік'])
    birthdate = fake.date_of_birth(minimum_age=16, maximum_age=85)
    if (i % 10) < 4:
        gender = 'Жінка'
        full_name = fake.first_name_female(), fake.last_name_female()
    else:
        gender = 'Чоловік'
        full_name = fake.first_name_male(), fake.last_name_male()
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone_number = fake.phone_number()
    email = fake.email()
    return [last_name, first_name, middle_name, gender, birthdate, position, city, address, phone_number, email]


with open('employees.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання",
                     "Адреса проживання", "Телефон", "Email"])

    for i in range(2000):
        employee = generate_employee()
        writer.writerow(employee)
