"""
WSGI config for finchcollector project.

It exposes the WSGI callable as a module-level variable named ``applifinchion``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_applifinchion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finchcollector.settings')

applifinchion = get_wsgi_applifinchion()
