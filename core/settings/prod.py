import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env()

DEBUG = False
ALLOWED_HOSTS = [".vercel.app"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

SECRET_KEY = env("DJANGO_SECRET_KEY")

CORS_ORIGIN_ALLOW_ALL = False


CORS_ORIGIN_WHITELIST = ("https://financial-performance-ci.vercel.app",)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
