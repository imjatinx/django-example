"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tj^evi2^$ys#1u@cca0zw+=_#2bey)lo!r6qq6nq++d=1#2+n$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["198.15.119.123", "booleantech.org", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['post/templates/'],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'blog',
#         'USER': 'admin',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': 3306,
#         'OPTIONS': {'charset': 'utf8mb4'},
#      }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Define the directory for log files
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# FORMATTERS = (
#     {
#         "standard": {
#             "format": "{levelname} {asctime:s} {module} {filename} {lineno:d} {name} {message}",
#             "style": "{",
#         },
#     },
# )


# HANDLERS = {
#     "error_handler": {
#         "class": "logging.handlers.RotatingFileHandler",
#         "filename": f"{BASE_DIR}/logs/debug.log",
#         "mode": "a",
#         "encoding": "utf-8",
#         "formatter": "standard",
#         "backupCount": 5,
#         "maxBytes": 1024 * 1024 * 10,  # 10 MB
#     },
#     'console': {
#         'class': 'logging.StreamHandler',
#         'formatter': 'standard',
#     },
# }

# LOGGERS = (
#     {
#         "django": {
#             "handlers": ["error_handler"],
#             "level": "WARNING",
#             "propagate": False,
#         },
#     },
# )


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": FORMATTERS[0],
#     "handlers": HANDLERS,
#     "loggers": LOGGERS[0],
#     'root': {
#         'level': 'DEBUG',
#         'handlers': ['console'],
#     }
# }

import logging

# FORMATTERS = {
#     "standard": {
#         "format": "{levelname} {asctime:s} {module} {filename} {lineno:d} {name} {message}",
#         "style": "{",
#     }
# }

# HANDLERS = {
#     "error_handler": {
#         "class": "logging.handlers.RotatingFileHandler",
#         "filename": f"{BASE_DIR}/logs/debug.log",
#         "mode": "a",
#         "encoding": "utf-8",
#         "formatter": "standard",
#         "backupCount": 5,
#         "maxBytes": 1024 * 1024 * 10,  # 10 MB
#     },
#     'console': {
#         'class': 'logging.StreamHandler',
#         'formatter': 'standard',
#     }
# }

# LOGGERS = {
#     "django": {
#         "handlers": ["error_handler"],
#         "level": "WARNING",
#         "propagate": False,
#     }
# }

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": FORMATTERS,
#     "handlers": HANDLERS,
#     "loggers": LOGGERS,
#     'root': {
#         'level': 'DEBUG',
#         'handlers': ['console'],
#     }
# }


import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{levelname} {asctime} {module} {filename} {lineno} {name} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
