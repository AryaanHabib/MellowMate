import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key for Django
SECRET_KEY = 'your-secret-key'

# Debug Mode (Should be False in Production)
DEBUG = True

# Allow All Hosts (Should be restricted in Production)
ALLOWED_HOSTS = ['*']

# Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Required for session handling
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # For Django REST Framework
    'corsheaders',  # For CORS Handling
    'chat',  # Your custom app
]

# Middleware Configuration
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Enable CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for session handling
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Session Configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Use database-backed sessions
SESSION_COOKIE_NAME = 'mellowmate_session'  # Optional: Custom session cookie name
SESSION_SAVE_EVERY_REQUEST = True  # Ensures session is saved on every request

# CORS Configuration
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (Dev only, restrict in production)

# URLs
ROOT_URLCONF = 'mellowmate_backend.urls'

# Templates
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

# WSGI Application
WSGI_APPLICATION = 'mellowmate_backend.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Authentication
AUTH_PASSWORD_VALIDATORS = []  # Dev Only (Add proper validators in production)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Files
STATIC_URL = 'static/'

# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
