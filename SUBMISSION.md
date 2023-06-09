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