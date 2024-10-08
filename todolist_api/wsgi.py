"""
WSGI config for todolist_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist_api.settings')
sys.path.append('/path/to/your/virtualenv/lib/python3.12/site-packages')
application = get_wsgi_application()
