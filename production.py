#
#   Production settings
#

from .base import *

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

ALLOWED_HOSTS = ['www.example.co.uk']

DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where collectstatic puts files
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_DIR), 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# email settings
EMAIL_HOST = env['EMAIL_HOST']
EMAIL_PORT = env['EMAIL_PORT']
EMAIL_HOST_USER = env['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env['DEFAULT_FROM_EMAIL'] # e.g 'Admin <noreply@example.com>'
SERVER_EMAIL = EMAIL_HOST_USER

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
 
ADMINS = ((env['ADMIN_NAME'], env['ADMIN_EMAIL']),)

CSRF_COOKIE_SECURE = True
