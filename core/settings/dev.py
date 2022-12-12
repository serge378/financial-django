DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

CORS_ORIGIN_ALLOW_ALL = True

SECRET_KEY = "django-insecure-f3)2@t@2!q*i$$s2i7!6tr=zmhf2n!p@!ak_19)hvfdzpv#$z)"

DEBUG = True
ALLOWED_HOSTS = []

CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)
