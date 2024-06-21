cd <your folder name>
git clone https://github.com/supershegs/inventory.git


# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install the packages listed in your requirements.txt
pip install -r requirements.txt

# run the app
python manage.py runserver