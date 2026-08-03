from .common import *



INSTALLED_APPS = [
    'daphne',
    'drf_spectacular'
] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'HOST': DB_HOST,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'PORT': DB_PORT
    }
}




CORS_ALLOW_CREDENTIALS = True