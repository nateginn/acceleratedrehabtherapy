from settings.common import *

SESSION_COOKIE_DOMAIN = None
CSRF_COOKIE_DOMAIN = None
ALLOWED_HOSTS = "*"

DEBUG = False

ROOT_URLCONF = 'urls.dev_common'

DATABASES.update({
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'acceleratedrehabtherapycom',
        'USER': 'postgres',
        'PASSWORD': 'postgres',  # Replace this with your actual PostgreSQL password
        'HOST': 'db',  
        'PORT': '5432',
    }
})

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",  
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,  
        }
    }
}

VARIATION_THREADS = 2

PIPELINE['SASS_ARGUMENTS'] = '-t nested'

STATICFILES_FINDERS += (
    'libs.pipeline.debug_finder.PipelineFinder',
)

# Google Maps API
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', '')

# Google reCAPTCHA
RECAPTCHA_PUBLIC_KEY = '6Lf_vxMjAAAAAA1X8_o_jVE8xI5G8z9ZrEnZ3KzZ'
RECAPTCHA_PRIVATE_KEY = '6Lf_vxMjAAAAAPsTCP8z_rCDxCIai_uMdiLx4yT8'

# =========
#  Logging
# =========
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'datefmt': '%d-%m-%Y %H:%M:%S',
            'format': '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s',
        },
        'server': {
            '()': 'libs.logging.formatters.SQLFormatter',
            'datefmt': '%d-%m-%Y %H:%M:%S',
            'format': '[%(asctime)s] %(message)s',
        },
        'file': {
            '()': 'libs.logging.formatters.UTCFormatter',
            'datefmt': '%d-%m-%Y %H:%M:%S',
            'format': '[%(asctime)s] %(levelname)-8s %(name)s\n'
                      '%(message)s'
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'server': {
            'class': 'logging.StreamHandler',
            'formatter': 'server',
        },
        'debug_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'logs', 'debug.log')),
            'maxBytes': 1024*1024,
            'backupCount': 5,
            'formatter': 'file',
        },
        'errors_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'logs', 'errors.log')),
            'maxBytes': 1024*1024,
            'backupCount': 2,
            'level': 'ERROR',
            'formatter': 'file',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
        },
        'django.db': {              # лог SQL-запросов
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['server'],
            'propagate': False,
        },
        'debug': {
            'handlers': ['console', 'debug_log'],
            'propagate': False,
            'level': 'DEBUG',
        },
        '': {
            'handlers': ['console', 'errors_log'],
            'level': 'INFO',
        }
    }
}
