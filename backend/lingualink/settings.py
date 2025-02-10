from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-f^b6afkw@akk4f6(8rq#=6x^-$dsh&5tf_r0&5s0nb$101s64('
DEBUG = True

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
    'user',
    'quiz'
]

#Authentication Token

REST_FRAMEWORK = { 
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.authentication.CookieTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
} 


ROOT_URLCONF = 'lingualink.urls'

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

WSGI_APPLICATION = 'lingualink.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lingualink',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  
        'PORT': '3307',      
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

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#CORS






# CORS settings
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# CORS settings (Only allow requests from frontend)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
    'http://127.0.0.1:8000',
]

# CSRF Trusted Origins (If using CSRF protection)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
]

# Enable credentials (for authentication)
CORS_ALLOW_CREDENTIALS = True

# Allowed HTTP methods
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

# Middleware (Make sure 'corsheaders.middleware.CorsMiddleware' is at the top)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware should be first
    'lingualink.middleware.BlockUnauthorizedOriginsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


