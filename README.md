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

**Heroku setup:** Strider will setup a new application on Heroku and do a git push to Heroku after each successful test run (if configured to 'deploy on green'). At this time, Strider does not run any 'one time' commands such as 'syncdb' or 'migrate'. You will need to run both of these commands before your project will run properly on Heroku.  

The easiest way to do so is to install the [Heroku Toolbelt](https://toolbelt.heroku.com/), point the toolbelt at the right app, and then execute the commands from the command line like so:

1) 'heroku run python manage.py syncdb --noinput'

2) 'heroku run python manage.py migrate'

For more details on running Django projects on Heroku, see [Getting Started with Django on Heroku/Cedar](https://devcenter.heroku.com/articles/django)

Strider is a hosted continuous deployment platform for Python and node.js. Learn more at [StriderApp.com](http://striderapp.com).