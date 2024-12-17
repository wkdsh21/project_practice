import os

from config.settings.base import *
from dotenv import load_dotenv

load_dotenv('../../envs/.env.prod')

ENV = load_dotenv('../../envs/.env.prod')


# SECURITY WARNING: keep the secret key used in production secret!
from django.core.management.utils import get_random_secret_key
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ENV['ALLOWED_HOSTS'].split(', ')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv('POSTGRES_HOST', 'localhost'),
        "NAME": os.getenv('POSTGRES_DBNAME', 'oz_practice'),
        "USER": os.getenv('POSTGRES_USER', 'postgres'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD', '0000'),
        "PORT": os.getenv('POSTGRES_PORT', '5432'),
    }
}

STATIC_URL = "static/"