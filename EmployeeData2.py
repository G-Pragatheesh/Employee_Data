from faker import Faker
import mysql.connector
from mysql.connector import errorcode
import datetime
import random


def generate_transcation_date():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return start_date + datetime.timedelta(days=random_days)


fake = Faker()
try:
    cnx = mysql.connector.connect(user='root',password ='Ranger@*123',host='localhost',database='praga')
    cursor = cnx.cursor()

    for _ in range(10):
        transaction_Date = generate_transcation_date()
        employee_id = random.randint(1,51)
        amount = round(random.uniform(100.00,5000.00), 2)
        insert_query = ("INSERT INTO Transactions "
                        "(EmployeeID,Amount , TransactionDate) "
                        "VALUES (%s, %s, %s)")
        insert_data = (employee_id,amount,transaction_Date)
        cursor.execute(insert_query,insert_data)

    cnx.commit()
    cursor.close()
    cnx.close()
    
    print('Data inserted succesfully')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)