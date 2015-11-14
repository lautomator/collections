##Collections

Here are a few Django-powered apps that track inventory and keep notes.
They are:

* Publications: books
* Reader: blog
* About (a static page)

###Setup
To get this going:
* Install Postgres and create a database locally
* Adjust Django settings, accordingly
* Install virtualenv and install the requirements:

```
source venv/bin/activate
pip install -r requirements.txt

```
- Run the Django server

`python jm_collections/manage.py runserver`

If all goes well you can create a user account to work with locally. If not, check the database configuration, including the connection and dev passwords. Be sure all of the virtualenv requirements are set.
