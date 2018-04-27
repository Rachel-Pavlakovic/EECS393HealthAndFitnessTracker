# EECS393HealthAndFitnessTracker

Web application that allows users to track things like their water intake, diet, and exercise.
Users have the option to set up alerts and reminders for things like drinking or working out and can analyse their habits over time.

# To set up virtual environment (Mac/Linux):
1. `python3.6 -m venv venv`
2.  `source venv/bin/activate`
3.  `pip install -r requirements.txt`
4. start developing
5. run `deactivate` when finished

# To set up virtual environment (Windows):
1. Install to your python `pip install virtualenv`
2. Setup environment folder `virtualenv venv`
3. Start virtual environment `source venv/Scripts/activate`
4. `pip install -r requirements.txt`
5. start developing
6. run `deactivate` when finished

# Adding new packages
1. `pip install (new package)`
2. `pip freeze > requirements.txt`
3.  everyone else rerun `pip install -r requirements.txt`

# To start the website
In the virtual environment: `python manage.py runserver`

# To run tests
In the virtual environment: `python manage.py test`

# To run tests with code coverage
In the virtual environment: `coverage run --source='.' manage.py test`
                            `coverage report`

