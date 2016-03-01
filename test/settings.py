SECRET_KEY = 'qaz123'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'sorl.thumbnail',
    'tastypie_sorl_thumbnail',
    'tastypie',
    'test',
]

ROOT_URLCONF = 'test.urls'

MEDIA_URL = '/media/'
