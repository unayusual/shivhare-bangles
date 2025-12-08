"""
WSGI config for shivhare_store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Load .env file if it exists (for local development)
try:
    from dotenv import load_dotenv
    # Use the project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent
    env_path = BASE_DIR / '.env'
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shivhare_store.settings')

application = get_wsgi_application()

# Vercel requires the WSGI application to be named 'app'
app = application
