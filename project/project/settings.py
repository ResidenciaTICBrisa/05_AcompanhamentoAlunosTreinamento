from pathlib import Path
import os
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tn_bk%@%rt@570m)e14wxmm4u2x_z&lvb8uh3--6ay7@h2olcs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_logs',
    'app',
    'backend',
    'bootstrap_modal_forms',    
]

PGHISTORY_CONFIG = {
    'schema_name': 'automatec',
    'history_table_suffix': '_history',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
                
            'libraries':{
                'first_letters': 'app.templatetags.custom_filters',
                
                }
        },
        
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
file_path = "/home/ubuntu/Desktop/devfront/devfull/postgre.txt"
with open(file_path, 'r') as file:
        password_database = file.readline().strip()

file_path = "/home/ubuntu/Desktop/devfront/devfull/passemail.txt"
with open(file_path, 'r') as file:
        password_email = file.readline().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'automatec',
        'USER': 'automauser',
        'PASSWORD': password_database,
        'HOST': '0.0.0.0',
        'PORT': '5432',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# DATABASES = {
# 'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'automatec',
#         'USER': 'automauser',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     },
#     'finatec': {
#         'ENGINE': 'sql_server.pyodbc',
# 		'HOST': '(LocalDB)\ProjectLocalDB',
# 		'PORT': '',
# 		'NAME': 'my_db',
# 		'USER': 'my_user',
# 		'PASSWORD': 'my_password',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # 'OPTIONS': {
        #     'message': "A senha é similar as informações do usuário.",
        # },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # 'OPTIONS': {
        #     'min_length': 8,
        #     'message': "A senha deve ter pelo menos %(min_length)d caracteres.",
        # },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # 'OPTIONS': {
        #     'message': "A senha é muito simples.",
        # },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # 'OPTIONS': {
        #     'message': "A senha não pode conter apenas números.",
        # },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'assets/'
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "app/static")
# ]

STATIC_URL = '/static/'
STATIC_ROOT = '/home/05_PipelineFinatec/sites/public/static'
MEDIA_ROOT = 'home/05_PipelineFinatec/sites/public/static/imagem'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# configurando email de recuperacao
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = "sistemas.finatec@finatec.org.br"
EMAIL_HOST_PASSWORD = password_email


