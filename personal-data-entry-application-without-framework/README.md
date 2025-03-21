# personal-data-entry-application-without-framework

This is a simple web application for entering and displaying personal data. It is built using Python without any server-side or client-side frameworks. The application uses the http.server module for handling HTTP requests and mysql.connector for database interactions.

**Features**

**Data Entry Form:** Users can enter personal data (Name, Surname, Telephone, Address, Age).
![image](https://github.com/user-attachments/assets/d9d205a2-7756-42fb-b413-e6b0f445639e)


**Data Validation:** Ensures all fields are filled, telephone is 8 digits, and age is a number.
![image](https://github.com/user-attachments/assets/f3fe2c47-f0ae-4e78-a414-3b2670b29888)

**Data Storage:** Stores entered data in a MySQL database.
![image](https://github.com/user-attachments/assets/a6800891-ef32-43e0-afcf-9a60858a958a)


**Data Display:** Displays all entered data in a table on the same page.

![image](https://github.com/user-attachments/assets/07247680-5bdd-4817-b5c3-33ed3cb53b5e)

**Prerequisites**

Before running the application, ensure you have the following installed:

Python 3.x (Download from python.org).

MySQL Server (Download from MySQL).

mysql-connector-python (Install via pip: pip install mysql-connector-python).

**Setup Instructions**

**1. Clone the Repository**
Clone this repository to your local machine: **git clone https://github.com/Dinesh-2311/personal-data-entry-application-without-framework.git**

**cd personal-data-entry-application-without-framework**

**a. Set Up the MySQL Database**
Log in to MySQL:
mysql -u root -p

![Screenshot 2025-03-22 000906](https://github.com/user-attachments/assets/e35c04e8-ba2e-4470-81c3-67b923e12aea)


**b. Create a database named personal_data:**

CREATE DATABASE personal_data;
USE personal_data;
![image](https://github.com/user-attachments/assets/b14f4f5c-70c0-41a2-8514-3e2507a235a6)


**c. create a table:**

CREATE TABLE persons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    telephone VARCHAR(15) NOT NULL,
    address VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

![image](https://github.com/user-attachments/assets/b1d53beb-fb75-475b-a27d-981e15a7b780)

**3. Update Database Configuration**
Open server.py and update the database connection details: conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="xxxxxxx",  # Replace with your MySQL password
    database="personal_data"
)

**Running the Application**
Start the server: python server.py
![image](https://github.com/user-attachments/assets/0fd47afa-da23-4e3e-96a4-4f54352ab402)


**Open your browser and navigate to:**
http://localhost:8000

![image](https://github.com/user-attachments/assets/f1358944-1a35-4af8-b9cc-ba389db842b6)

Use the form to enter personal data. The data will be saved in the database and displayed in the table below the form.
![image](https://github.com/user-attachments/assets/6c4961d4-4844-46de-a190-8a6fc85335b1)


**Project Structure**
![image](https://github.com/user-attachments/assets/cb36b219-4b89-4750-8f4a-921d8ff45171)

**Key Files**

**index.html:** Contains the HTML form and table for displaying data.

**server.py:** Handles HTTP requests, validates data, and interacts with the MySQL database.

**styles/style.css:** Custom styles for the form and table.


**Dependencies**
mysql-connector-python: Used for connecting to and interacting with the MySQL database.
Install it using: **pip install mysql-connector-python**

**Troubleshooting**

**Database Connection Issues:** Ensure MySQL is running and the credentials in server.py are correct.

**Port Conflicts:** If port 8000 is already in use, change the port in server.py: python

**Future Improvements**

Add error messages for invalid input.

Implement user authentication and authorization.

Use a templating engine for dynamic HTML generation.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

