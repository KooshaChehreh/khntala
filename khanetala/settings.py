"""
Django settings for kahnetala project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+ux@-o$2(t5v!$!_ta1%_a++32lc^fvqc!b17+%5ek&=#di6fo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["91.107.240.53"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    "users",
    "transaction",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'khanetala.urls'

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

WSGI_APPLICATION = 'khanetala.wsgi.application'

# PASSWORD HASHERS

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres', 
        'PASSWORD': 'yourpassword', 
        'HOST': 'db', 
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'users.permissions.IsAuthenticatedWithToken',
]
}

# JWT Settings

# mention that these keys should be in env file of production

JWT_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCWKw7hx0s4Xa2h
WQQk3RNopzG9MHV416jf2PdWrzl8ppIWlMPFqyiRiC3lGz7kDql54x4/8CKxFAt/
BjJuh7UnVF9JT7gNgqe3bE8n1RgWzLyUaYJ/08llKB9VTAsh3nxGbcp1vd5q/Wh8
xlyIHNnvhWDrV67/KNIUJWhfuSNLMSu3PPvJmiz8ncxybOgZnkQCrZwxFDZyQL6f
3GyrhmRNEpwDKCOXqaBDSLHZ2cFQiY2B+an5hqOC6biBbmzH80d7sA/cJl0Mkm8h
M8r0+m6r5AAakp8qHrb4Qa+5O+wNKcqNrxxQnoIqzBuFvkGQf2StkK40ZajzXMOh
xsK9CPJfAgMBAAECggEADkZtlbzyQ5t0JABoSnDRpYMvUULICALIRO9FI/JoTpcv
EAJ4UdQheSQu6LacVeWm6rVSbNWRFrBHH34hUSyJZgG5RSjU4EPpWaBsLect8Qzp
aFpXU3t4i6syv1MJQ+D4g2Fwe5zfBeCtDB93MGE9vm05d2XQduUUg2HC+EaLOlx+
+eL5UeAv2ds93e4NlSwJOZrJs59QF2nc9i8CCodtVeN8qpHZa+CSuuJ3Qn9/slyv
8cCBK1LzHEKhgUJgCv4MbKQlQxiHqkW5bByJzqae5tz5lz5m/HvJi8X8pi9wt77x
fM/+eU3NIIWQahVM3Ax9TLHarDv9IJxo0KXHfMwMIQKBgQDF81RYynLSQMR3gbxj
FndQodNubp7UfGZVyNIVm/emf8OuqT3V5YztJNBgrkk7QbJIvR7GVFwm/c6W93pX
Jrt55EBk1VWmu7xB234qcpHWmNOHrSHBdgXOZLcI8/3h4GBKfxSOiRXEEPQSgH1Y
5Ue6klD/eawBrEKUlGdDjkqbiQKBgQDCNJVq/sNZVbuXyfwQ1mDKjFOXbhjbO4vT
whXBGImRx6+iO9Cpq3ScS1/8J0KGJVffVkzr3tqBJ5el26X1B3MpxcOUtDrcf3Wf
15X9aNUDBAeoft0sewfQL6BUlJYaUPYoNqXspb7iKn+malmwe37xo6AG6HlUk7dC
UmHf42acpwKBgQCfyMPsDDbU+szb/pA3l7nmD0pg2NBCisv8MOdL5CLqdjVZdmlg
kDPKdK3zbJvWRjiIOIhv5UahfrxU5h0N3kj0okdMXVwPA3l525gi4WpRQ/lzilA2
HnOfX3LTukfUHU78s0m/qG42Xsz1ZlxH9oOI2XSiU++BRjBUSNp2EJSuqQKBgQC8
JsHUZXrRpFQZHSHPFkO0OPwLrCj8zdYMlO8Ko0E1MaehoB3rJCfX/NbDry2uVaOq
xyvDIafElZ1AnWtN16flgqqX+X1Ff19wOygf2V72iwL4ZeDWZWQOePX2u/YpDONP
1pIuke47pD0D9+lpKFy2s3Yo+zYBkRNtd+9HQEN75QKBgBvNnhZfEqMxRP0Kwzol
W6A0Z+ydjlzRWDILvSm1OvcogilcY4On92yHXmCQVmd5X6Kf3GevC0nNm+w8vuOb
W5975zrr/PoR66zUGKfffoscxaybbTrn6a9XEps7bCMbhpSkLE6h8cL001kCf4Hh
2dDbhXV3sc9ckwhKYQv8ywaR
-----END PRIVATE KEY-----"""

JWT_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlisO4cdLOF2toVkEJN0T
aKcxvTB1eNeo39j3Vq85fKaSFpTDxasokYgt5Rs+5A6peeMeP/AisRQLfwYyboe1
J1RfSU+4DYKnt2xPJ9UYFsy8lGmCf9PJZSgfVUwLId58Rm3Kdb3eav1ofMZciBzZ
74Vg61eu/yjSFCVoX7kjSzErtzz7yZos/J3McmzoGZ5EAq2cMRQ2ckC+n9xsq4Zk
TRKcAygjl6mgQ0ix2dnBUImNgfmp+Yajgum4gW5sx/NHe7AP3CZdDJJvITPK9Ppu
q+QAGpKfKh62+EGvuTvsDSnKja8cUJ6CKswbhb5BkH9krZCuNGWo81zDocbCvQjy
XwIDAQAB
-----END PUBLIC KEY-----
"""

JWT_SECRET_KEY = "jdhf$82!kjsdf#23hfd&3rksjdf@94hsdfsd^23jdfgk@42jhdslf_9fksd!"
JWT_EXPIRATION_SECS = 20 * 60

PRICE_PER_GRAM_RIALS = 10000000


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#         },
#         "elasticsearch": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#         },
#     },
# }