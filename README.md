Klingsbo - A sample Django app for Strider & Heroku
===================================================

Klingsbo was built by following along with the Django Tutorial, and then adding tests inspired by Daniel Lindsley's excellent tutorial on Django testing:

part 1: http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/
part 2: http://toastdriven.com/blog/2011/apr/17/guide-to-testing-in-django-2/

Klingsbo uses South for database migrations, PostgreSQL as the production database, and Gunicorn as the production webserver. 

To setup Klingsbo:

1) run 'pip install requirements.txt' from within the project directory.

2) run 'python manage.py syncdb --noinput'

3) run 'python manage.py migrate'

Migrate will load the initial_data.json file which creates an admin user and the first poll. The admin username is 'admin' and the password is 'abc123'. 
