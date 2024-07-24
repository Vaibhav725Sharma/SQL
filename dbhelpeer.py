import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="First_project"
            )
            self.mycursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Some error occurred: {err}")
        else:
            print("Connected to the database")
