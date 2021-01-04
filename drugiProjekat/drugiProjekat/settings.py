import os
import poverljivo as pov


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = pov.BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = pov.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = pov.DEBUG

ALLOWED_HOSTS = pov.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = pov.INSTALLED_APPS

MIDDLEWARE = pov.MIDDLEWARE

ROOT_URLCONF = pov.ROOT_URLCONF

TEMPLATES = pov.TEMPLATES

WSGI_APPLICATION = pov.WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = pov.DATABASES


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = pov.AUTH_PASSWORD_VALIDATORS


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = pov.LANGUAGE_CODE

TIME_ZONE = pov.TIME_ZONE

USE_I18N = pov.USE_I18N

USE_L10N = pov.USE_L10N

USE_TZ = pov.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = pov.STATIC_URL
