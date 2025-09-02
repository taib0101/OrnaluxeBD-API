from pathlib import Path
import dj_database_url
import os
import sys

from swagger import SPECTACULAR_DEFAULTS
from typing import Dict, Any
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i3d-3gwag*@65pv63k8sj$-h2kd62b7n1h^gmc#z8km59z%vu@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database URL
DATABASE_URL = (
    os.getenv("DEVELOPMENT_DATABASE_URL")
    if sys.argv[2].lower() == "development"
    else os.getenv("PRODUCTION_DATABASE_URL")
)

# Secret Key for JWT Token
SECRET_TOKEN_KEY = (
    os.getenv("DEVELOPMENT_SECRET_TOKEN_KEY")
    if sys.argv[2].lower() == "development"
    else os.getenv("PRODUCTION_SECRET_TOKEN_KEY")
)

# Secret Algorithm for JWT Token
SECRET_TOKEN_ALGO = (
    os.getenv("DEVELOPMENT_SECRET_TOKEN_ALGO")
    if sys.argv[2].lower() == "development"
    else os.getenv("PRODUCTION_SECRET_TOKEN_ALGO")
)



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',

    'src',
    'swagger'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL, # local host: postgres://root:1234@localhost:5432/mydatabase
        conn_max_age=None # keeps single connection for all quires + transactions session
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Rest Framework
# Edited By Taib, Inspired By: https://github.com/tfranzel/drf-spectacular/?tab=readme-ov-file
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "src.supports.handlers.handle_result"
}

# Django Rest Framework Spectacular 
SPECTACULAR_SETTINGS: Dict[str, Any] = SPECTACULAR_DEFAULTS
