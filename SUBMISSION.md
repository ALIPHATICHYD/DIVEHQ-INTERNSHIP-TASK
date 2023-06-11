# Commands to set up the repo (dependencies etc.)
To setup the repo, you will need to install the following dependencies:
```
pip install -r requirements.txt
```

# Commands to run the test suite
To run the test suite, you can use the following command:
```
python -m unittest discover
```

# Commands to run the API server
To run the API server, you can use the following command:
```
uvicorn app:app --reload
```

# Setting up the Project
* Creating a virtual environment 
```
python -m venv venv
```

* Activating the Virtual Environment
```
source venv/bin/activate
```

* Installing Django Framework
```
pip install django djangorestframework djoser drf-yasg
```

* Installing a Django Project 
```
django-admin startproject dive
```

```
cd dive
```

```
python manage.py startapp users
```


* Adding Installed apps to settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    <!-- add these apps below 👇🏾 -->
    'users',
    'rest_framework', 
    'djoser',
    'drf_yasg',
]
```

* create a new file called 'urls.py' in users folder


* Running it on the server
```
python manage.py runserver
```


Django-admin startproject is to create a project that uses Django features, then we needed to create apps with Django and we use the command python manage,py startapp users
but before this, we need to cd into the django admin project we created. Then, in the setting file of the Django project, we need to tell Django that there are apps that we have been installed, and we need to use 
so we register users, rest_framework, djoser, drf_yasg



# Setting up the Database using SQLite Manager
* Installing SQLite Manager
```
pip install pysqlite3
```

* Creating a new file called 'models.py' in users folder

* Creating a new file called 'admin.py' in users folder

* Creating a new file called 'serializers.py' in users folder

* Creating a new file called 'views.py' in users folder

* Creating a new file called 'urls.py' in users folder

* Creating a new file called 'tests.py' in users folder

* Creating a new file called 'urls.py' in dive folder

* Creating a new file called 'urls.py' in dive folder



# Setting up the Database using SQLite Manager
* Installing SQLite Manager
```
pip install pysqlite3
```

After running the server for a Django project, the next step for the SQLite manager would typically involve performing database operations using Django's ORM (Object-Relational Mapping) or directly interacting with the SQLite database. However, we will be using the Django REST Framework to create a RESTful API for our project.

