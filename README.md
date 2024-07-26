SQL Practice: Flipkart User Management System
Project Overview
The Flipkart User Management System is a simple command-line application that demonstrates basic user registration, login, and profile management functionalities using Python and MySQL. This project is an excellent example for beginners to understand database integration and basic CRUD operations.

Features
User Registration
Users can register by providing their name, email, and password.
User Login
Registered users can log in using their email and password.
Profile Management
After logging in, users can:
View their profile details.
Edit their profile (feature currently not available).
Delete their profile.
Log out from their account.
Screenshots



![Screenshot 2024-07-24 233242](https://github.com/user-attachments/assets/cf3af54e-6eda-492e-a092-d03041de7ed5)
![Screenshot 2024-07-24 235622](https://github.com/user-attachments/assets/8a9d72e0-7f3d-49d0-a726-9c7d6081f327)

Project Structure

flipkart.py

Flipkart Class:

__init__: Initializes the database connection and displays the main menu.
menu: Displays the main menu and navigates to the registration or login process based on user input.
login_menu: Displays the user profile management menu after successful login.
register: Handles user registration by collecting user details and saving them to the database.
login: Handles user login by verifying user credentials and navigating to the profile management menu.
dbhelper.py
DBhelper Class:
__init__: Establishes a connection to the MySQL database.
register: Inserts new user details into the users table.
search: Retrieves user details based on email and password for login verification.


Future Improvements

Profile Editing: Implement the profile editing feature.
Password Encryption: Use hashing for storing passwords securely.
Input Validation: Add input validation to prevent SQL injection and ensure data integrity.
