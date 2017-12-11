"""
Django settings for digitalclerk project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y_m*)433eud(dm+@2-+0$-8%w@sh^4ko7!y#=q#7jq8)s&+^s+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# /*** This wildcard pattern is only used for local development only! ***/
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'digitalclerk_app.apps.DigitalclerkAppConfig',
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
    # 'digitalclerk_app.middleware.AutoLoginRedicrect',
]

ROOT_URLCONF = 'digitalclerk.urls'

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

WSGI_APPLICATION = 'digitalclerk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'digitalclerk',
        'USER': 'postgres',
        'PASSWORD': 'sejarahsux',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email Setup
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'digitalclerktest@gmail.com' 
EMAIL_HOST_PASSWORD = 'sejarahsux1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# OAuth2.0 settings
UCLAPI_URL = "https://uclapi.com"
UCLAPI_CLIENT_ID = "2427587556461725.8961107549887679"
UCLAPI_URL = "https://uclapi.com"
UCLAPI_CLIENT_SECRET = "d35f152647087eee2d36885cef33ce3597f2fd6faacbbb7db48dcfab5fae4799"

# Config for user profiles
MODULE_DETAIL_DASHBOARD_PROFILE = 'LECTURER_PROFILE' # Sets the profile for the dashboard page of each module
OFFICE_HOUR_DASHBOARD_STUDENT_PROFILE = 'STUDENT_PROFILE_1' # Sets the student user profile that raises a request
OFFICE_HOUR_DASHBOARD_STAFF_PROFILE = 'LECTURER_PROFILE' # Sets the lecturer who is in charge of dealing with request in an office hour

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Oauth2.0 token session states
SESSION_TOKEN_LOGGED_OUT = "logged_out"
SESSION_TOKEN_LOGGING_IN = "logging_in"

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
