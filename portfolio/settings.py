import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Security Settings
SECRET_KEY = 'votre-cle-secrete-ici'
DEBUG = True  # Passez à False en production
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Ajoutez votre domaine ou IP en production

# Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Vos applications
    'projects',  # Remplacez par le nom réel de votre app si différent
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL Configuration
ROOT_URLCONF = 'portfolio.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Répertoire des templates
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
WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Changez si vous utilisez une autre base de données
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'fr-fr'  # Langue française
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ **Configuration des fichiers statiques**
STATIC_URL = '/static/'  # URL publique pour les fichiers statiques
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Répertoire contenant vos fichiers statiques
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Destination pour `collectstatic`

# ✅ **Configuration des fichiers médias**
MEDIA_URL = '/media/'  # URL publique pour les fichiers uploadés
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Répertoire pour stocker les fichiers uploadés

# ✅ **Ajout des fichiers médias et statiques uniquement si DEBUG est activé**
if DEBUG:
    from django.conf.urls.static import static
    urlpatterns = []  # Correction pour éviter l'erreur d'import dans `urls.py`
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ **Logging (facultatif pour déboguer)**
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}