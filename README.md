# opaalaAPI
This is for sharing my test code in Python - Django

# Bring Code to your PC
1. git clone https://github.com/mehsan1/opaalaAPI.git

# Requirements
1. Python 3.9 or greater

# Install packages
1. create virtual environment (python -m venv <myenvpath>)
2. activate virtual environemtn (source .venv/bin/activate)
3. pip install -r /path/to/requirements.txt

# Configurations
1. MySQL Database setting in settings.py
2. once you ahve updated and your db server is up, you can run migrations
3. please change CORS_ORIGIN_WHITELIST in settings.py according to URL for front end
4. please change ALLOWED_HOSTS in settings.py according to URL for front end

# run migrations
1. python manage.py migrate api 

# run application
1. python manage.py runserver 

# Help with packages
You might get problem with packages so, there is a way to handle this by trying different ways of commands

just for your help and examples below commands

1. python -m pip install PyMySQL
2. python -m pip install django-cors-headers
3. python -m pip install corsheader
4. python -m pip install djangorestframework
5. pip3 install django-injector
