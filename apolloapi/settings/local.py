import os

# Base settings configuration
from .base import *

# Installed apps local to dev env
from .installed import *

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://*"
]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]
CSRF_COOKIE_DOMAIN = "*"

print("----------- DEVELOPMENT SANDBOX -----------")
# DATABASE
if SYSTEM_ENV == "GITHUB_WORKFLOW":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("ENGINE", "django.db.backends.postgresql"),
            "NAME": os.environ.get("POSTGRES_NAME", "postgres"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        }
    }
