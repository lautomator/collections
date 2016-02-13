##Collections

Here are a few Django-powered apps that track inventory and keep notes.
They are:

* Publications: books
* Reader: blog
* About (a static page)

###Local Setup
To get this going:
* Install Postgres and create a database called 'collections'
* Adjust Django settings, accordingly (see **configuration**, below)
* Install virtualenv and install the requirements:

`source env/bin/activate`

`pip install -r requirements.txt`

A **configuration file** must be created to store your development secrets. You could also create other conifg files for testing, staging, and production. You will need to define the following vars in that file:

```
sk = '<string>'
usr = '<string>' # refers to the user who created the database 'collections'
pwd = '<string>' # refers to the pwd for that user
```

You can, of course, include any other configuration variables that you like here.

The configuration file needs to live in the virtual environment `env/lib/python2.7/`. You can setup a symlink here if you prefer to keep the file else. This will vary from system to system.

The file in `settings.py` is called `dev_config`. It is imported into the settings file. After your configuration variables are set up, you can proceed:

* Run the Django server:
`python jm_collections/manage.py runserver`

###Troubleshooting
* Check the database configuration, including the connection and dev passwords. 
* Be sure all of the virtualenv requirements are set.
* Check the path and/or symlink to make sure that your configuration file is imported into the settings (`seettings.py`).
