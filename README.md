# yummyRecipes [![Build Status](https://travis-ci.org/otim22/yummyRecipes.svg?branch=master)](https://travis-ci.org/otim22/yummyRecipes) . [![Coverage Status](https://coveralls.io/repos/github/otim22/yummyRecipes/badge.svg?branch=master)](https://coveralls.io/github/otim22/yummyRecipes?branch=master)

This a simple flask application

## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly.
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2.
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create virtual environments.
* **[Pylint]** – or linting and ensure your work follows PEP8 style guide requirements.
* And other dependencies on requirements.txt.

## Installation / Usage
* To run your own build, ensure python3 is globally installed in your computer. If not, get python3 [here](https://www.python.org).
* Ensure you have installed virtualenv globally otherwise run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ https://github.com/otim22/yummyRecipes
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd yummyRecipe
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ source venv/bin/activate
        ```

* #### Install your requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```
    
* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ flask run
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/
    
* #### Running the tests
    On your terminal, run tests:
    ```
    (venv)$ nosetests test_bank_account.py
    ```
    
 * #### Deployment
    OThis app is deloped on heroku:
    ```
    https://dashboard.heroku.com/apps/yummyrecipesv1
    ```   
    
## Versioning

We use [git](http://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/otim22/yummyRecipes). 

## Authors

* **OtimFredrick** - *Initial work*


    
  
