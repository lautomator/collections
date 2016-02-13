"""Django settings for jm_collections project."""

import dev_config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = dev_config.sk

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
    'signup',
    'books',
    'reader',
    'info',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'USER': dev_config.usr,
        'PASSWORD': dev_config.pwd,
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

LOGIN_URL = [os.path.join(BASE_DIR, '/signup/login/')]
