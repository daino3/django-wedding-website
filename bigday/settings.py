"""
Django settings for bigday project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u7!-y4k1c6b44q507nr_l+c^12o7ur++cpzyn!$65w^!gum@h%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guests.apps.GuestsConfig',
    'wedding.apps.WeddingConfig',
    'django_extensions',
    'rest_framework',
    'import_export',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bigday.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join('bigday', 'templates'),
        ],
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

WSGI_APPLICATION = 'bigday.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = BASE_DIR + '/static_root'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bigday/static'),
    os.path.join(BASE_DIR, 'photo/uploads'),
)

# Beware: Django sucks with media
# web browser location
MEDIA_URL = '/media/'

# the address your emails (save the dates/invites/etc.) will come from
DEFAULT_WEDDING_FROM_EMAIL = 'You and Your Partner <happilyeverafter@example.com>'
# the default reply-to of your emails
DEFAULT_WEDDING_REPLY_EMAIL = 'happilyeverafter@example.com'

# when sending test emails it will use this address
DEFAULT_WEDDING_TEST_EMAIL = DEFAULT_WEDDING_FROM_EMAIL
WEDDING_CC_LIST = []  # put email addresses here if you want to cc someone on all your invitations

try:
    from .localsettings import *
except ImportError:
    pass


LOG_FORMAT = '{}[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s{}'
LOG_DATEFMT = '%a %Y-%m-%d %H:%M:%S%z'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'custom': {
            'format': LOG_FORMAT.format('', ''),
            'datefmt': LOG_DATEFMT
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'custom',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.db': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',  # noisy
        },
        'bigday': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'guests': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'wedding': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
