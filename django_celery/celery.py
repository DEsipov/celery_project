#!-*-coding:utf-8-*-
import os

from celery import Celery

# Добавляем путь к конфигу django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

# Именуем наше приложение celery. Его мы будем передавать первым параметром
# при запуске сельдерея.
# python -m celery -A django_celery worker
# см. доки
# https://docs.celeryq.dev/en/stable/reference/cli.html#cmdoption-celery-A
app = Celery('django_celery')

# Говорим. что все настройке сельдерея будут лежать в файле settings.py
# и иметь префик CELERY_XXX
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery пробегает по проекту, ищет все файлы tasks.py и определяет там
# функции, как задачи.
app.autodiscover_tasks()
