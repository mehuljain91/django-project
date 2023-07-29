# Django Project

This is a Django web application that allows you to manage users and their details. Users can be viewed and added using the provided routes.

## Setup and Run

### Prerequisites
- Python 3.x (Install from https://www.python.org/)
- MySQL (Install from https://dev.mysql.com/downloads/)

### Installation

1. Clone the repository.
```
git clone https://github.com/mehuljain91/django-project.git
cd django-project
```

2. Install django using pip.
```
pip install django
```
3. Configure the database settings:

Open django-project/settings.py and set up the database configuration. By default, this application uses MySQL. Ensure you have MySQL installed and create a new database named "users". Update the database configuration with your MySQL credentials.

4. Apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
```
5. Run the development server:
```
python manage.py runserver
```

The application will be accessible at http://127.0.0.1:8000/.

## Database Schema and Sample Data

The application uses a MySQL database. To set up the database schema, follow these steps:

1. Create a MySQL database with the name "users".
```
CREATE DATABASE users;
```

2. Design a table named "users" with the following columns:
- id (INT, Primary Key)
- name (VARCHAR)
- email (VARCHAR)
- role (VARCHAR)

The SQL code to create the "users" table is as follows:
```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(100)
);
```

3. To populate the "users" table with sample data, you can run the following SQL queries:
```
INSERT INTO users (name, email, role)
VALUES
    ('John Doe', 'john@example.com', 'Admin'),
    ('Jane Smith', 'jane@example.com', 'User'),
    ('Mike Johnson', 'mike@example.com', 'User');
```

## Git Workflow and Contribution

1. Create a new branch for each feature or bug fix.
2. Make changes in your branch and commit them.
3. Push your branch to the remote repository.
4. Submit a pull request to merge your changes into the main branch.
5. Once approved, the changes will be merged into the main branch.  

To contribute to the project:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make changes and commit them to your branch.
5. Push your branch to your forked repository.
6. Create a pull request from your branch to the main repository's main branch.
7. Once approved, your changes will be merged into the main repository.
