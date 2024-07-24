import sys
from dbhelper import DBhelper

class Flipkart:

  def __init__(self):
    #connect to the data base
    self.db = DBhelper()
    self.menu()

  def menu(self):

    user_input = input("""
    1. Enter 1 to regester
    2. Enter 2 to login 
    3. Anything else to leave
    """)

    if user_input=="1":
      self.register()
    elif user_input=="2":
      self.login()
    else:
      sys.exit(1000)

  def register(self):
    name = input("Enter the Name: ")
    email = input("Enter the Email: ")
    password = input("Enter the Password: ")

    response = self.db.register(name,email,password)

    if response:
      print("Registration successful")
    else:
      print("Registration Unsuccessful")
    self.menu()


obj = Flipkart()

