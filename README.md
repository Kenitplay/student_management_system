# Student Management System

A simple Django-based web application for managing student records. This system allows you to add, view, edit, and delete student information. It also includes a search feature and responsive design for all devices.

Features:
- Add Students: Add new students with their first name, last name, email, and student ID.
- View Students: View a list of all students in a responsive table.
- Edit Students: Update student information.
- Delete Students: Remove students from the system.
- Search Students: Search for students by name, email, or student ID.
- Responsive Design: Works seamlessly on all devices (desktop, tablet, and mobile).


# Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package installer)
- Git (for cloning the repository)
- Pipenv (For Environment)

# Installation

Follow these steps to set up the project on your local machine:

1. Clone the Repository
Open your terminal and run the following command to clone the repository:
- https://github.com/Kenitplay/student_management_system.git

2. Navigate to the Project Directory
Change to the project directory:
- cd student_management_system

3. Create a Virtual Environment
Install dependencies and create a virtual environment using Pipenv:
- pipenv install

4. Activate the virtual environment:
- pipenv shell

5. Set Up the Database:
- python manage.py migrate


# Running the Application

Start the Django development server:
- python manage.py runserver

Open your web browser and navigate to:
- http://127.0.0.1:8000/


