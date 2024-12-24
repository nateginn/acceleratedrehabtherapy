import os
import re
import sys
from django.utils.translation import ugettext_lazy as _
from .pipeline import PIPELINE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps_common'))

SECRET_KEY = '@pc(!n(8tgg33&=f%v9s1gnfl+3i)(h$7bl_t&fs&6a$&br-fd'

DEBUG = False

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)

TIME_ZONE = 'America/Denver'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'ajax_views',
    'admin_honeypot',
    'captcha',
    'django_cron',
    'django_jinja',
    'mptt',
    'pipeline',
    'solo',
    'suit_ckeditor',
    
    # Apps
    'main',
    'blocks',
    'about',
    'blog',
    'contacts',
    'services',
    'users',
    'base_page',
    
    # Apps common
    'admin_ctr',
    'admin_log',
    'attachable_blocks',
    'breadcrumbs',
    'backups',
    'ckeditor',
    'footer',
    'gallery',
    'google_maps',
    'header',
    'menu',
    'paginator',
    'rating',
    'seo',
    'social_networks',
    'testimonials',
    
    # Libs
    'libs.autocomplete',
    'libs.color_field',
    'libs.file_field',
    'libs.form_helper',
    'libs.jinja2',
    'libs.management',
    'libs.pipeline',
    'libs.stdimage',
    'libs.templatetags',
    'libs.variation_field',
    'libs.sprite_image',
)

# Suit
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Accelerated Rehab Therapy',
    
    # search
    'SEARCH_URL': '',
    
    # menu
    'MENU': (
        {
            'app': 'main',
            'icon': 'icon-file',
            'models': (
                'MainPageConfig',
            )
        },
        {
            'app': 'about',
            'icon': 'icon-file',
            'models': (
                'LocationPageConfig',
                'TeamPageConfig',
                'AboutPageConfig',
            )
        },
        {
            'app': 'blog',
            'icon': 'icon-file',
            'models': (
                'BlogPost',
                'BlogConfig',
            )
        },
        {
            'app': 'services',
            'icon': 'icon-file',
            'models': (
                'Service',
            )
        },
        {
            'app': 'testimonials',
            'icon': 'icon-file',
            'models': (
                'Testimonial',
            )
        },
        {
            'app': 'contacts',
            'icon': 'icon-file',
            'models': (
                'Message',
                'Address',
                'ContactsConfig',
            )
        },
        '-',
        {
            'app': 'config',
            'icon': 'icon-lock',
            'models': (
                'Config',
            )
        },
        {
            'app': 'social_networks',
            'icon': 'icon-lock',
            'models': (
                # 'FeedPost',
                'SocialLink',
                'SocialConfig',
            )
        },
        '-',
        {
            'icon': 'icon-lock',
            'label': 'Authentication and Authorization',
            'permissions': 'users.change_customuser',
            'models': (
                'auth.Group',
                'users.CustomUser',
            )
        },
        {
            'app': 'backups',
            'icon': 'icon-hdd',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'django_cron',
            'icon': 'icon-hdd',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'admin',
            'icon': 'icon-list-alt',
            'label': _('History'),
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'sites',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'seo',
            'icon': 'icon-tasks',
            'permissions': 'users.admin_menu',
            'models': (
                'SeoConfig',
                'Redirect',
                'Counter',
                'Robots',
            ),
        },
    ),
}

# Pipeline
SASS_INCLUDE_DIR = os.path.join(BASE_DIR, 'static', 'scss')
PIPELINE['SASS_BINARY'] = 'sassc --load-path ' + SASS_INCLUDE_DIR
PIPELINE['SASS_ARGUMENTS'] = '-t nested'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'libs.cache.middleware.SCCMiddleware',
    'libs.middleware.utm.UTMMiddleware',
    'menu.middleware.MenuMiddleware',
    'seo.middleware.RedirectMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
)

ALLOWED_HOSTS = ()

ROOT_URLCONF = 'urls.common'

WSGI_APPLICATION = 'project.wsgi.application'

# Sites and users
SITE_ID = 1
ANONYMOUS_USER_ID = -1
AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'main:index'
LOGIN_REDIRECT_URL = 'main:index'
RESET_PASSWORD_REDIRECT_URL = 'main:index'
LOGOUT_URL = 'main:index'

# Email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'webmaster@localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'webmaster@localhost'
EMAIL_SUBJECT_PREFIX = '[%s] ' % (SUIT_CONFIG['ADMIN_NAME'], )

# ==================================================================
# ==================== APPS SETTINGS ===============================
# ==================================================================

# Honeypot
ADMIN_HONEYPOT_EMAIL_ADMINS = False

BACKUP_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'backup'))
PUBLIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'public'))

# Django solo caching
SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 10 * 60

# Smart Cache-Control
SCC_IGNORE_URLS = [
    r'/admin/',
    r'/dladmin/',
]

VALUTE_FORMAT = None

# Django Cron
CRON_CLASSES = [

]

# ==================================================================
# ==================== END APPS SETTINGS ===========================
# ==================================================================

SESSION_COOKIE_DOMAIN = None
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 30 * 24 * 3600
CSRF_COOKIE_DOMAIN = None

DISALLOWED_USER_AGENTS = ()

ADMINS = ()
MANAGERS = ()
IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

DATABASES = {}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'VERSION': 1,
        'KEY_PREFIX': 'django',
        'KEY_FUNCTION': 'project.utils.cache_key_func',
        'REVERSE_KEY_FUNCTION': 'project.utils.reverse_key_func',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

TEMPLATES = [
    {
        'BACKEND': 'libs.jinja2.Jinja2Backend',
        'DIRS': (
            os.path.join(BASE_DIR, 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'match_regex': r'.*\.(html|xml)$',
            'exclude_regex': r'.*(admin|admin_honeypot|suit|registration)/.*',
            'app_dirname': 'templates',
            'undefined': 'libs.jinja2.UndefinedSilently',
            'extensions': [
                'jinja2.ext.i18n',
                'jinja2.ext.loopcontrols',
                'django_jinja.builtins.extensions.CsrfExtension',
                'django_jinja.builtins.extensions.StaticFilesExtension',
                'django_jinja.builtins.extensions.TimezoneExtension',
                'django_jinja.builtins.extensions.DjangoFiltersExtension',
                'django_jinja.builtins.extensions.DjangoExtraFiltersExtension',
            ],
            'context_processors': (
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'social_networks.context_processors.google_apikey',
                'libs.context_processors.domain',
            ),
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            'templates',
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'social_networks.context_processors.google_apikey',
            ),
        }
    },
]

RECAPTCHA_PUBLIC_KEY = '6Lf3aaMUAAAAAETYWwcM-Le99_elue4-xxdepsIj'
RECAPTCHA_PRIVATE_KEY = '6Lf3aaMUAAAAAMlXjYnHq4psOUymP8yL9XfNt9m6'

# Locale
LOCALE_PATHS = (
    'locale',
)

# Datetime formats
FORMAT_MODULE_PATH = [
    'project.formats',
]

# Media
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
