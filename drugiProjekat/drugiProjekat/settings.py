import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIN_REDIRECT_URL = '/articles'

SECRET_KEY = 'z+)ko^irgyspmw915h%04f%l+&-pwoych^0)l(xk1bl+e(6$ms'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baza.apps.BazaConfig',
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

ROOT_URLCONF = 'drugiProjekat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', os.path.join(BASE_DIR, 'baza/templates')]
        ,
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

WSGI_APPLICATION = 'drugiProjekat.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sava_baza',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'




# from PoverljivoDIR import poverljivo as pov
#
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = pov.BASE_DIR
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = pov.SECRET_KEY
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = pov.DEBUG
#
# ALLOWED_HOSTS = pov.ALLOWED_HOSTS
#
#
# # Application definition
#
# INSTALLED_APPS = pov.INSTALLED_APPS
#
# MIDDLEWARE = pov.MIDDLEWARE
#
# ROOT_URLCONF = pov.ROOT_URLCONF
#
# TEMPLATES = pov.TEMPLATES
#
# WSGI_APPLICATION = pov.WSGI_APPLICATION
#
#
# # Database
# # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
# DATABASES = pov.DATABASES
#
#
# # Password validation
# # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = pov.AUTH_PASSWORD_VALIDATORS
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/3.0/topics/i18n/
#
# LANGUAGE_CODE = pov.LANGUAGE_CODE
#
# TIME_ZONE = pov.TIME_ZONE
#
# USE_I18N = pov.USE_I18N
#
# USE_L10N = pov.USE_L10N
#
# USE_TZ = pov.USE_TZ
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.0/howto/static-files/
#
# STATIC_URL = pov.STATIC_URL
