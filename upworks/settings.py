from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^1d*62&ouug%pq=l_ot^=w%sb+%idz@9r-59wdlc^gp1vo0m9("

# Aplicaciones base
BASE_APPS = [
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Aplicaciones locales
LOCAL_APPS = [
    'apps.users',
    'apps.main',
]

# Applicaciones de terceros
THIRD_APPS = [
    'rest_framework',
    'simple_history',
    # 'drf_yasg',
    # 'corsheaders',
]

# Application definition
INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = "upworks.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "upworks.wsgi.application"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    { "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]


# Internationalization
LANGUAGE_CODE = "es-MX"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost",
    "http://127.0.0.1",
    "http://192.168.0.254",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.127.0.0.1",
    r"^https://\w+\.192.168.0.254",
]


# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Libreria para PostgreSQL
#         'NAME': 'upworks',  # Nombre de la base de datos PostgreSQL
#         'USER': 'postgres',  # Usuario de la base de datos PostgreSQL
#         'PASSWORD': '*****',  # Contraseña de usuario PostgreSQL
#         'HOST': '127.0.0.1',  # Ubicacion de la base de datos
#         'DATABASE_PORT': '5432',  # Puerto utilizado
#     }
# }

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'