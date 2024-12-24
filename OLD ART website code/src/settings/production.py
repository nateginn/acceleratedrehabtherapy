from settings.common import *

DOMAIN = '.acceleratedrehabtherapy.com'
PROJECT_ROOT = '/var/www/acceleratedrehabtherapy.com'

SESSION_COOKIE_DOMAIN = DOMAIN
CSRF_COOKIE_DOMAIN = DOMAIN

SECRET_KEY = '8wi-v@owdvyjfs(1_*bb#w4n7re6(b4^!=s50_20c$(^w9jr@_'

ALLOWED_HOSTS = (
    DOMAIN,
)

ROOT_URLCONF = 'urls.production'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
BACKUP_ROOT = os.path.join(PROJECT_ROOT, 'backup')
PUBLIC_DIR = os.path.join(PROJECT_ROOT, 'public')

DATABASES.update({
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'CONN_MAX_AGE': 60,
    }
})

# Google Maps API
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']

# =========
#  Logging
# =========
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
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
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'debug_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.abspath(os.path.join(os.path.join(PROJECT_ROOT, 'logs'), 'debug.log')),
            'maxBytes': 1024*1024,
            'backupCount': 5,
            'formatter': 'file',
        },
        'errors_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.abspath(os.path.join(os.path.join(PROJECT_ROOT, 'logs'), 'errors.log')),
            'maxBytes': 1024*1024,
            'backupCount': 5,
            'level': 'WARNING',
            'formatter': 'file',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
        },
        'django.server': {
            'handlers': ['null'],
            'propagate': False,
        },
        'debug': {
            'handlers': ['debug_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['errors_log', 'mail_admins'],
        }
    }
}
