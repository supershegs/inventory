cd <your folder name>
git clone https://github.com/supershegs/inventory.git


# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install the packages listed in your requirements.txt
pip install -r requirements.txt


# To ensures that the database structure matches the structure defined by the Django models of this app

python manage.py makemigrations
python manage.py migrate


# The superuser account has special privileges and permissions within the Django project(username and password)
python manage.py createsuperuser


# Click on the link below to access the API postman Collection

https://documenter.getpostman.com/view/4152080/2sA3XWdeba

# To generate the API key

send request you request body with username and password to http://127.0.0.1:8000/api-token-auth/ to get your API


# run the app
python manage.py runserver


