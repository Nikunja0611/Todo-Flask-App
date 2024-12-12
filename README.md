# Flask TODO App

## Overview

This is a simple **TODO Application** built using the **Flask Framework** and **MySQL** for managing and storing tasks. The app allows users to add, view, and delete their to-dos easily through an intuitive web interface.

---

## Features

- **Add Tasks**: Users can input a title and description to create a new task.
- **View Tasks**: All tasks are displayed in a table format with details such as title and description.
- **Delete Tasks**: Users can remove completed or unwanted tasks from the list with a click.
- **Responsive Design**: Clean and minimal interface for better usability.

---

## Technologies Used

- **Backend**: Flask (Python Framework)
- **Frontend**: HTML, CSS, and Bootstrap for styling.
- **Database**: MySQL for storing TODO tasks.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>

2. **Activate virtual environment**:
    ```bash
    cd path/to/your/project
    source ./env/Scripts/activate.bat

3. **Set Up the Database:**:
    ```mysql
- **Install following libraries**:
    pip install mysql-connector
    pip install mysql-connector-python
    pip install pymysql

- **Edit App config**:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@localhost/todo"

- **Create a database and table in MySQL**:   
    CREATE DATABASE IF NOT EXISTS todo;
    USE todo;

    CREATE TABLE IF NOT EXISTS todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(200));

4. **Run the Flask Application**:
    python app.py

5. **Access the app**:
    http://127.0.0.1:5000

## Usage
- Fill out the Todo Title and Todo Description fields and click Submit to add a task.
- View the task in the table below.
- Use the Delete button in the action column to remove a task.

![Todo-Flask-App](image.png)