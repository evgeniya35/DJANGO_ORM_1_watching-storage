import os
from dotenv import load_dotenv, find_dotenv
from distutils.util import strtobool

load_dotenv(find_dotenv())
TOKEN = os.environ.get('TOKEN')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(strtobool(os.environ.get('DEBUG').lower()))

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
