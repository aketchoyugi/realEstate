# realEstate
Django-based website for real estate that offers a seamless and intuitive user experience, connecting buyers, sellers, and real estate agents in an efficient and effective manner. This platform provides comprehensive property listings, advanced search functionality, and interactive maps, enabling users to easily explore and discover their ideal properties. With a user-friendly interface, the website offers personalized profiles, saved searches, and notifications, ensuring a tailored experience for each user.

## Installation and Setup

Follow these steps to set up the project locally:

1. Clone the repository: `git clone https://github.com/aketchoyugi/realEstate.git`
2. Navigate to the project directory: `cd realEstate`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Linux/Mac: `source venv/bin/activate`
   - For Windows: `venv\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Configure the database in the `settings.py` file.
7. Apply database migrations: `python manage.py migrate`
8. Create a superuser for administrative access: `python manage.py createsuperuser`
9. Run the development server: `python manage.py runserver`
10. Access the website in your browser at `http://localhost:8000`


## Technology Stack

The Django Real Estate Website is built using the following technologies:

- Django
- Python
- HTML/CSS
- JavaScript
- PostgreSQL/ SQLite (or your preferred database management system)
