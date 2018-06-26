#
#   Dev settings
#

from .base import *

SECRET_KEY = 'NOT_THE_SAME_AS_PRODUCTION'

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

ALLOWED_HOSTS = ['*']