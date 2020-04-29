# Agile Stories and Tasks Time Tracker

This is a small django project suitable for estimating and tracking time of
the agile project management stories and tasks.

## Getting Started

Below you will find the instructions and requirements on how to install and run this project on your local machine.

### Installing

The first step is to clone the repository.
After that you can create a virtual environment, activate it and install the requirements.txt file:

```
python -m venv env
cd env/Scripts/activate.bat                 // for Windows users
source env/bin/activate                     // for OS X users
python -m pip install -r requirements.txt
```

After successful installation you can migrate and start the server:
```
python manage.py migrate
python manage.py runserver
```

## Testing

The tests are included in the application file 'tests'. There are two types of tests:
unit and integration. Integration tests requires a webdriver, for example, Chrome users need a chromedriver,
FireFox users need a geckodriver. In this case, geckodriver was used and it can be downloaded here:
```
https://github.com/mozilla/geckodriver/releases
```
Both of these categories have different tags, so it is possible
to run only unit, only integration, or all of the tests.   

**Note: to run the integration tests you need to have the server running.**

```
coverage run manage.py test --tag=integration   // only integration tests
coverage run manage.py test --tag=unit          // only unit tests
coverage run manage.py test                     // all tests
```

Coverage can help to understand which parts of the code are not tested. Run the command:
```
coverage html
```
And then open file 'index.html' in htmlcov folder.

