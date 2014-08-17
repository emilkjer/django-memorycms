import os

from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*+Gkm%d#i-nyzrl1u8rr0&1ge#a%3k!6cm)l&yuyhh2spa1v14'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['memorycms.moome.net',]

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'memorycms',
        'USER': 'memorycms',
        'PASSWORD': 'tohFio2Oshiiquiobu9ru5cah7IeZei2caijootheiRahpah9uc3loov8ja2athi',
        'HOST': '127.0.0.1',
        'PORT': '',
     }
 }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "../static")
