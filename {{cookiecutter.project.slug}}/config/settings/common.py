# -*- coding: utf-8 -*-
"""
Django settings.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ

ROOT_DIR = environ.Path(__file__) - 3  # (base_dir/config/settings/common.py - 3 = base_dir/)
PROJ_DIR = ROOT_DIR.path('dproject')

env = environ.Env()
env.read_env()

SECRET_KEY = env('DJANGO_SECRET_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'crispy_forms',
    'sorl.thumbnail',
    'compressor',
)

LOCAL_APPS = (
    
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEBUG = env.bool('DJANGO_DEBUG', False)

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
DEFAULT_FROM_EMAIL = env(
    'DJANGO_DEFAULT_FROM_EMAIL', default='django app <app@django.group>'
)

SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

ADMINS = (
    ("""{{cookiecutter.user.full_name}}""", '{{cookiecutter.user.email}}'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': env.db('DATABASE_URL', default='{{cookiecutter.db.dbms}}://{{cookiecutter.db.user}}@localhost/{{cookiecutter.db.name}}'),
}
#DATABASES['default']['ATOMIC_REQUESTS'] = True
if DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
    DATABASES['default']['OPTIONS'] = {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}


TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]
USE_I18N = True
LOCALE_PATHS = [
    PROJ_DIR('locale'),
    'locale',
]
USE_L10N = True
USE_TZ = True

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PROJ_DIR.path('templates')),
            "templates",
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'dproject.context_processors.is_debug_mode',
            ],
            'libraries': {
               'sorl_thumbnail': 'sorl.thumbnail.templatetags.thumbnail',
            },
        },
    },
]

STATIC_ROOT = str(PROJ_DIR('staticfiles'))
FILE_UPLOAD_TEMP_DIR = str(PROJ_DIR('tmp'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(PROJ_DIR.path('static')),
    'static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# 5MB MAX UPLOAD SIZE!
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

MEDIA_ROOT = str(PROJ_DIR('media'))
MEDIA_URL = '/media/'

ROOT_URLCONF = 'config.urls'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'config.wsgi.application'

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


# Third party settings start here jo.
CRISPY_TEMPLATE_PACK = 'bootstrap4'
