# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0964838/data/www/toping.ru/floors/')
sys.path.insert(1, '//var/www/u0964838/data/www/toping.ru/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangofloors.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#  /opt/python/python-3.9.0/bin/python -m poetry install