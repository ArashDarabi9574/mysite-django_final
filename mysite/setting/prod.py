from mysite.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vb_lh$1jpp^f-ikk@8rp@)u!s*wlu_j(fiod(p@h1pv#8=s+ql'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['arashdarabi.ir', 'www.arashdarabi.ir']


# INSTALLED_APPS = []




SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
SECURE_BROWSER_XSS_FILTER = True
## X-Frame-Options
X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'