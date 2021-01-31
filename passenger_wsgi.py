# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0964838/data/www/toping.ru/aminbot')
sys.path.insert(1, '/var/www/u0964838/data/DjangoToping/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangofloors.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()