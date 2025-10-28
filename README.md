# Django

## Create and activate a Python Virtual Environment in Windows
 
 - python -m venv <vm-name>
 - .\<vm-name>\Scripts\activate.bat

### Check the installtion is successfull py typing the command slmgr /xpr

 - You’ll get one of the following messages:
  - ✅ “This machine is permanently activated” → Windows is activated.

### Command to install django
 - pip install django

### Check installed version of django
 - django-admin --version

### Command to start a new Djang 
 - django-admin startproject <project_name>. (Avoid using - inside project name)

### Command to starts the Django development web server
 - python .\manage.py runserver

### Command to create a new app inside your project 
 - python manage.py startapp <new-app-name>

### Before starting to work on the new app follow : 
 - copy the url.py from the main project to the newely created app folder
 - update the url.py to include the import of 'include' and update the 
  - eg: ![alt text](image.png)

### DB creation and Migration
 - add data to Models.py file, each class inside a model file represent a table inside the db.sqlite
 - python manage.py makemigrations
 - python manage.py mirgate
 - ##### delete a column from table is as easy as deleting it from the modles.py and then running the <python manage.py makemirgtions & python manage.py migrates> commands. 

### Login and Add tables to Django Administartaion
 - import models to admin.py file using import statement <from . models import *>
 - register the model by typing <admin.site.register(student)> in the admin.py file
 - creat the super user by giving the command < python manage.py creatsuperuser>
    - input proper username and pwd
 - run the sever by giving the command python manage.py runserver
 - login to Django Admin panel by giving the username and pwd    
 - #### dumping data command <python manage.py dumpdata --output=datadump.json --indent 2> creates a dumpdata.json file with all data from the DB.
  - edit the settings.py DATABASES sction with following fields and values 
        DATABASES = { 
          'default': { 
              'ENGINE': 'django.db.backends.mysql', 
              'NAME': 'Student_Management_Db',          
              'USER': 'root',             # Your MySQL username 
              'PASSWORD': 'root',  # Your MySQL password 
              'HOST': 'localhost',        # Usually localhost 
              'PORT': '3306',             # Default MySQL port 
              'OPTIONS': { 
                  'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 
              }, 
          } 
      } 

        

