"""
Django settings for jm_collections project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# This is a development key only
SECRET_KEY = 'dev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'books',
    'reader',
    'info',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jm_collections.urls'

WSGI_APPLICATION = 'jm_collections.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'collections',
        'USER': 'john',
        'PASSWORD': 'dev',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '~/Documents/Programming/python/django-projs/jm_collections/static/',
)

STATIC_URL = os.path.join(BASE_DIR, 'static/')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates/')]
