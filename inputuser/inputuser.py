import mysql.connector


def insert_data(first_name, last_name, course, age):
    try:
        conn = mysql.connector.connect(
        host = "localhost",
        user="root",
        password = "",
        database = "input_user"
        )
        cursor = conn.cursor()

        query = "INSERT INTO tblinputuser (first_name, last_name, course, age) VALUES (%s, %s, %s, %s)"

        values = (first_name, last_name, course, age)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

        print("Data Successfully Inserted")

    except Exception as e:
        print("Not successfully", str(e))








while True:
    first_name = input("Enter your name: ")
    last_name = input("Enter your last name : ")
    course = input("Enter your course : ")
    age = input("Enter your age : ")

    insert_data(first_name, last_name, course, age)

