import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ZtbW#LOvM?D3f1B6pCnx44KiR|C45s4M2~@~jdHLdw9?~'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# Настройка почты

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "NAME": 'u0964838_floors_bd',
        "USER": 'u0964838_floors',
        "PASSWORD": 'u0964838floorsbd',
        "HOST": 'localhost',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

