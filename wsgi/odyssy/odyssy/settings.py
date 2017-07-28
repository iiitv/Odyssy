"""
Django settings for myproject project.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import secrets
from socket import gethostname


DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)

ON_OPENSHIFT = 'OPENSHIFT_PYTHON_IP' in os.environ

sys.path.append(os.path.join(REPO_DIR, 'libs'))
SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not ON_OPENSHIFT

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [
        gethostname(),
        os.environ.get('OPENSHIFT_APP_DNS'),
        'odyssy.singhpratyush.in',
    ]
    # This will allow cookies  to be sent only via HTTPS connections.
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = (
    'admission.apps.AdmissionConfig',
    'academic.apps.AcademicConfig',
    'people.apps.PeopleConfig',
    'institute.apps.InstituteConfig',
    'photologue',
    'sortedm2m',
    'taggit',
    'events.apps.EventConfig',
    'news.apps.NewsConfig',
    'basic.apps.BasicConfig',
    'tag.apps.TagConfig',
    'careers.apps.CareersConfig',
    'more.apps.MoreConfig',
    'announcement.apps.AnnouncementConfig',
    'gallery.apps.GalleryConfig',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'odyssy.urls'

STATICFILES_DIRS = [
    WSGI_DIR + "/media",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'odyssy.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('OPENSHIFT_POSTGRESQL_DB_NAME', 'odyssy'),
        'USER': os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME', 'odyssy'),
        'PASSWORD': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD',
                                   'odyssy'),
        'HOST': os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT', '5432'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(WSGI_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(WSGI_DIR, 'media')

# Redirects HTTP requests to HTTPS.
# However, it is suggested to write a rewrite rule for this action.
SECURE_SSL_REDIRECT = True
