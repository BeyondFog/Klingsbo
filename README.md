## Klingsbo - A sample Django app for Strider & Heroku

Klingsbo was built by going through the Django Tutorial, and then adding tests inspired by Daniel Lindsley's excellent tutorial on Django testing ([part one](http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/), [part two](http://toastdriven.com/blog/2011/apr/17/guide-to-testing-in-django-2/)).

Klingsbo uses [South](http://south.aeracode.org/) for database migrations, PostgreSQL as the production database, and [Gunicorn](http://gunicorn.org/) as the production webserver. 

To setup Klingsbo on your dev box:

1) create and activate a virtualenv

2) run 'pip install -r requirements.txt' from within the project directory.

3) run 'python manage.py syncdb --noinput'

4) run 'python manage.py migrate'

The 'migrate' command will load the initial_data.json file which creates an admin user and the first poll. The admin username is 'admin' and the password is 'abc123'. 

### Notes:

**Database setup:** Klingsbo is configured to use PostgreSQL locally (ie on your dev box) and also when running the test suite on Strider. There is a sqlite dev configuration commented out in settings.py should you wish to to use sqlite locally instead of PostgreSQL. Heroku will add its own block of code to settings.py for production PostgreSQL.

**Heroku setup:** Strider will setup a new application on Heroku and do a git push to Heroku after each successful test run (if configured to 'deploy on green'). Strider will also run 'syncdb' and 'migrate' after each code push.


For more details on running Django projects on Heroku, see [Getting Started with Django on Heroku/Cedar](https://devcenter.heroku.com/articles/django)

Strider is a hosted continuous deployment platform for Python and node.js. Learn more at [StriderApp.com](http://striderapp.com).