# README

A starting set of settings files for a Django project. Set the default DJANGO_SETTINGS_MODULE value in wsgi.py and manage.py to point to the dev settings file then in production you can set DJANGO_SETTINGS_MODULE to point to the production file. 

In the settings files you will need to:
* replace <PROJECT_NAME> with your project name
* replace <YOUR_DATABASE_NAME> with the name of your database (currently set up for Postgres)
* fill in a SECRET_KEY for the dev settings file
* fill in ALLOWED_HOSTS in the production settings file