import os 

INSTALLED_APPS = (
    'corsheaders',
    'dal', 'dal_select2',
    'admin_auto_filters',
    'modeltranslation',


    'jet.dashboard',
    'jet',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',

    "mptt",
    "tinymce",
    'ckeditor', 'ckeditor_uploader',
    'allauth','allauth.account','allauth.socialaccount', 'allauth.socialaccount.providers.google',
    'import_export',
    'rosetta',
    'colorfield',
    'adminsortable2',
    "rest_framework", 'rest_framework.authtoken',
    "rangefilter",
    'debug_toolbar',
    'nested_admin',

    
    'editors',
    'people',
    'core',
    'menu',


    
    'sw_shop',
)
X_FRAME_OPTIONS = 'SAMEORIGIN'
SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = "config.get('common', 'secret_key')"
DEBUG = True 
ALLOWED_HOSTS = ['*']
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]
ROOT_URLCONF = 'application.urls'
WSGI_APPLICATION = 'application.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ("uk","uk"),
    ("ru","ru"),
    ("en","en"),
]
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
JET_DEFAULT_THEME = 'default'
JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default'
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
# JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'
JET_MODULE_YANDEX_METRIKA_CLIENT_ID = '46de85bff0f94c82bbf42be177f128a2'
JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET = '01107ac1049b49ab9b24e60e95ba2a93'
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')
# CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
