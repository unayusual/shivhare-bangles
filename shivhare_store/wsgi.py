"""
WSGI config for shivhare_store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shivhare_store.settings')

application = get_wsgi_application()

app = application
