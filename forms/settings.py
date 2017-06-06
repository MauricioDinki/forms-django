"""
Django settings for forms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
import environ
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

env = environ.Env()

SECRET_KEY = '$+ybuwq*b2j=t%3mq&*n@lsr_#y7k9)n3js1vrth+6)p$t3wj0'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'forms.urls'

WSGI_APPLICATION = 'forms.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default="CHANGE")
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="CHANGE")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="CHANGE")
AWS_S3_HOST = env("AWS_S3_HOST", default="CHANGE")

STATICFILES_STORAGE = 'app.custom_storages.StaticStorage'
STATIC_URL = env("STATIC_URL", default="CHANGE")

DEFAULT_FILE_STORAGE = 'app.custom_storages.MediaStorage'
MEDIA_URL = env("MEDIA_URL", default="CHANGE")
