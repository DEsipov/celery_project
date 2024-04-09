from .celery import app as celery_app


# Насильно инициируем объект celery.
__all__ = ('celery_app', )
