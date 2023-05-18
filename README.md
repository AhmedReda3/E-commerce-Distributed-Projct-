# E-commerce-Distributed-Projct-
Design a distributed online software system.

## Project Setup Instructions

This project is developed using Django and PostgreSQL. Please follow the instructions below to set up and run the project on your local machine.

### Prerequisites

- Python 3.x: Make sure Python is installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

- PostgreSQL: Install PostgreSQL to set up the project's database. You can download it from the official PostgreSQL website: https://www.postgresql.org/download/

### Installation Steps

1. Clone the repository: 
   
   git clone <repository_url>
   

2. Navigate to the project directory:
   
   cd <project_directory>
   

3. Create a virtual environment:
   
   python -m venv env
   

4. Activate the virtual environment:
   - For Windows:
     
     .\env\Scripts\activate
     
   - For macOS/Linux:
     
     source env/bin/activate
     

5. Install the project dependencies:
   
   pip install -r requirements.txt
   

6. Database Configuration:
   - Open the `settings.py` file located in the project's root directory.
   - Modify the database configuration according to your PostgreSQL setup. Update the `DATABASES` section with your database credentials.

7. Apply database migrations:
   
   python manage.py migrate
   

8. Create a superuser (admin):
   
   python manage.py createsuperuser
   

9. Run the development server:
   
   python manage.py runserver
   

10. Open a web browser and visit `http://localhost:8000` to access the application.

### Accessing the Admin Interface

The project includes an admin interface for managing data. To access the admin panel, follow these steps:

1. Start the development server if it's not already running:
   
   python manage.py runserver
   

2. Open a web browser and visit `http://localhost:8000/admin`.
   
3. Log in using the superuser credentials you created earlier.

### Additional Notes

- It's recommended to use Visual Studio Code as the IDE for this project. You can download it from the official website: https://code.visualstudio.com/

- While not required, pgAdmin can be useful for visualizing and managing the PostgreSQL database. You can download pgAdmin from: https://www.pgadmin.org/download/
