# CRUD-Database_App
This Python project is a CRUD (Create, Read, Update, Delete) application for managing employee records in a SQL database.

# Employee Database Management App

## Overview

This Python project is a CRUD (Create, Read, Update, Delete) app that manages records in a SQL database. The app focuses on the "employee" table within the "office" database. Whether you're learning database operations, working on a personnel management system, or building a similar project, this app provides practical examples of using PyMySQL to interact with a database.

## Features

- **Create Records:** Add new employee records to the database.
- **Read Records:** Retrieve and display employee records.
- **Update Records:** Modify employee information in the database.
- **Delete Records:** Remove employee records from the database.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pawanshukla0963/Python-EmployeeMgmtCRUD.git
   cd CRUD-Database_App

2. **Create Database in MySQL:**
    Open Xampp
    start MYSQL and open its shell
    Get it start by entering mysql -u root 
    by entering next commands create and use Database "Office"
 
    > Create database Office; <br>
    > use office;

3. **Create a table employee:**
    Now, being in database office we will need to create a table employee with columns Id, Firstname, Lastname, 
    Email, Address by following query.

    > Create table employee ( id int (5), FirstName varchar (15), LastName varchar (15), Email varchar (20), Address varchar (20));

4. **Run the crudapp.py file and execute queries through CRUD app**

## Database Setup:

- Make sure you have PyMySQL installed.
- Create a database named "office" if it doesn't exist.

## Usage:

- Run crudapp.py to launch the CRUD app for managing employee records.
- Follow the prompts to create, read, update, and delete employee records.

## Dependencies:

- Python 3.11.4
- PyMySQL
