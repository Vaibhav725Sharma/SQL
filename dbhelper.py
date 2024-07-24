import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect( host="localhost", user="root",    password="",  database="First_project"
            )
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occurred")
            sys.exit(0)
        else:
            print("Connected to the database")

    def register(self,name,email,password):
        try:
          query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
          values = (name, email, password)
          self.mycursor.execute(query, values)
          self.conn.commit()
        except:
          return -1
        else:
          return 1
