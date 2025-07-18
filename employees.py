import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="hadjilover911",
    database="DBconcentrix"
)

cursor = conn.cursor()

name = input("Enter name : ")
last_name = input("Enter last name : ")
age = int(input("Enter age :"))
address = input("Enter address :")

sql1 = "INSERT INTO tblemployees (name, last_name, age, address) VALUES(%s, %s, %s, %s)"
values = (name, last_name, age, address)
cursor.execute(sql1, values)

employee_id = cursor.lastrowid

salary = float(input("Enter salary : "))
prog_language = input("Enter langauge : ")

sql2 = "INSERT INTO tblinfo (employee_id, salary, prog_language) VALUES (%s, %s, %s)"
values = (employee_id, salary, prog_language)
cursor.execute(sql2, values)

conn.commit()

print("Successfully insert datas into both tables")

cursor.close()
conn.close()