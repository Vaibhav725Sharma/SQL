
# Flipkart User Management System
<body><h2>Project Overview</h2><p>The Flipkart User Management System is a simple command-line application that demonstrates basic user registration, login, and profile management functionalities using Python and MySQL. This project is an excellent example for beginners to understand database integration and basic CRUD operations.
        </p>
        <h2>Features</h2>
        <h3>User Registration</h3>
        <ul>
            <li>Users can register by providing their name, email, and password.</li>
        </ul>        <h3>User Login</h3>
        <ul>
            <li>Registered users can log in using their email and password.</li>
        </ul><h3>Profile Management</h3>
        <ul>
            <li>After logging in, users can:</li>
            <ul>
                <li>View their profile details.</li>
                <li>Edit their profile (feature currently not available).</li>
                <li>Delete their profile.</li>
                <li>Log out from their account.</li>
            </ul>
        </ul> <h2>Screenshots</h2>
        <img src="https://github.com/user-attachments/assets/cf3af54e-6eda-492e-a092-d03041de7ed5" alt="Registration Screenshot" class="screenshot">
        <img src="https://github.com/user-attachments/assets/8a9d72e0-7f3d-49d0-a726-9c7d6081f327" alt="Profile Management Screenshot" class="screenshot">
<h2>Project Structure</h2>
        <h3>flipkart.py</h3>
        <ul>
            <li><strong>Flipkart Class</strong>:</li>
            <ul>
                <li><code>__init__</code>: Initializes the database connection and displays the main menu.</li>
                <li><code>menu</code>: Displays the main menu and navigates to the registration or login process based on user input.</li>
                <li><code>login_menu</code>: Displays the user profile management menu after successful login.</li>
                <li><code>register</code>: Handles user registration by collecting user details and saving them to the database.</li>
                <li><code>login</code>: Handles user login by verifying user credentials and navigating to the profile management menu.</li>
            </ul>
        </ul>

  <h3>dbhelper.py</h3>
        <ul>
            <li><strong>DBhelper Class</strong>:</li>
            <ul>
                <li><code>__init__</code>: Establishes a connection to the MySQL database.</li>
                <li><code>register</code>: Inserts new user details into the <code>users</code> table.</li>
                <li><code>search</code>: Retrieves user details based on email and password for login verification.</li>
            </ul>
        </ul>



  <h2>How to Run the Project</h2>
        <ol>
            <li><strong>Install MySQL</strong>:
                <ul>
                    <li>Ensure you have MySQL installed and running on your machine.</li>
                </ul>
            </li>
            <li><strong>Setup Database</strong>:
                <ul>
                    <li>Create a database named <code>First_project</code>.</li>
                    <li>Create the <code>users</code> table using the schema provided above.</li>
                </ul>
            </li>
            <li><strong>Install Dependencies</strong>:
                <ul>
                    <li>Install the <code>mysql-connector-python</code> package using pip:</li>
                    <div class="code">
                        <pre>pip install mysql-connector-python</pre>
                    </div>
                </ul>
            </li>
            <li><strong>Run the Application</strong>:
                <ul>
                    <li>Execute the <code>flipkart.py</code> script to start the application:</li>
                    <div class="code">
                        <pre>python flipkart.py</pre>
                    </div>
                </ul>
            </li>
        </ol>

  <h2>Future Improvements</h2>
        <ul>
            <li><strong>Profile Editing</strong>: Implement the profile editing feature.</li>
            <li><strong>Password Encryption</strong>: Use hashing for storing passwords securely.</li>
            <li><strong>Input Validation</strong>: Add input validation to prevent SQL injection and ensure data integrity.</li>
        </ul>

</body>
</html>
