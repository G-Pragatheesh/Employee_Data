from faker import Faker
import mysql.connector
from mysql.connector import errorcode
import random
import datetime

# Function to generate random hire date
def generate_hire_date():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return start_date + datetime.timedelta(days=random_days)

# Function to generate random salary
def generate_salary():
    return round(random.uniform(30000.00, 120000.00), 2)

# Create Faker object
fake = Faker()

# Connect to MySQL database
try:
    cnx = mysql.connector.connect(user='root', password='Ranger@*123', host='localhost', database='praga')
    cursor = cnx.cursor()

    # Generate and insert random data
    for _ in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        department = random.choice(['Engineering', 'Marketing', 'HR', 'Finance', 'IT', 'Sales', 'Customer Service', 'Operations'])
        job_title = fake.job()
        salary = generate_salary()
        hire_date = generate_hire_date()
        address = fake.address()

        insert_query = ("INSERT INTO Employees "
                        "(FirstName, LastName, Email, PhoneNumber, Department, JobTitle, Salary, HireDate, Address) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        insert_data = (first_name, last_name, email, phone_number, department, job_title, salary, hire_date, address)

        cursor.execute(insert_query, insert_data)

    cnx.commit()
    cursor.close()
    cnx.close()

    print("Data inserted successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

