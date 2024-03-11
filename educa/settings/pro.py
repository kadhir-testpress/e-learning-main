from .base import *
DEBUG = False
ADMINS = (
 ('Antonio M', 'email@mydomain.com'),
)
ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': 'educa',
 'USER': 'kadhir',
 'PASSWORD': 'testpress1$',

 }
}
