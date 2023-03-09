# Online-Shop

## Table of contents
1. General info
2. Technologies
3. Setup
3.1. Run
3.2. Creating superuser to managing admin-panel
4. Status

## 1. General info
This project is an e-commerce platform designed for small businesses trading specialized in equipment-in this case, surveying equipment. In addition to the store layer, there is a blog-like sub-site. Its purpose is to be able to publish reviews of new products in the industry, events, news etc. The site can also be used for other purposes, not only surveying; the backend page is flexible enough to post any products and categories.

## 2. Technologies
Project is created with:
* Python 3.10
* Django 4.1.7
* HTML
* CSS
* SQLite

## 3. Setup
### 3.1. Run
* Clone a repository

* If you are using PyCharm, for example, then open the project and in the terminal create an isolated environment using the command: 
```
cd Online-shop
python -m venv myvenv
```
* Then you need to activate the virtual environment: 
```
cd myvenv/scripts/activate
```
* Then install the required packages included in the requirements.txt file using: 
```
pip install requirements.txt
```
* Migrate the databases: 
```
python manage.py makemigrations
python manage.py migrate
```
* Done, you can now start the development server with the command: 
```
python manage.py runserver
```
### 3.2. Creating superuser to managing in admin-panel
* In order to take full advantage of the project's functionality, a super user must be created. 
``` 
python manage.py createsuperuser
```
* Then we write the following credentials step by step. We can fill these credentials according to our preferences:

* Username:

Email address:

Password: ********

Password (again): ********

Note: After filling a row, press “Enter” to fill the other information.

The superuser will be created if all the fields are entered correctly.

## 4. Status

Project is in progress.