
from pathlib import Path
import os
from dotenv import load_dotenv

import dj_database_url

# Load .env file (important for local dev)

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
# =========================
# SECURITY
# =========================




SECRET_KEY = os.getenv("jlokat)_-%pkf7@m-t=d6owu0+7+2@8(nhq)z!0ola(@c$vgd*")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".vercel.app",
]

# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'crud'
    
    # your apps here
]

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # important for Vercel/static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"

# =========================
# DATABASE (NEON POSTGRES)
# =========================
DATABASE_URL = "postgresql://neondb_owner:npg_kJp0KBd5EoeT@ep-muddy-wind-atoer278-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

import dj_database_url

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
    )
}

# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =========================
# STATIC FILES (Vercel)
# =========================
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
# DEFAULT PRIMARY KEY
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# CSRF / SECURITY (IMPORTANT FOR ADMIN)
# =========================
CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
]

# Optional: for production domains
# CSRF_TRUSTED_ORIGINS += ["https://yourdomain.com"]