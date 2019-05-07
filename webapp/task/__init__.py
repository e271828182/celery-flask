# -*- coding=utf-8 -*-
from celery import Celery

celery = Celery()


def make_celery(app):
    celery.main = app.import_name
    # celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    # celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']
    # celery.__init__(
    #     app.import_name,
    #     backend=app.config['CELERY_RESULT_BACKEND'],
    #     broker=app.config['CELERY_BROKER_URL']
    # )
    celery.main = app.import_name
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    # celery.conf.result_backend = app.config['CELERY_BROKER_URL']
    if app.config.get('CELERY_BROKER_TRANSPORT_OPTIONS'):
        celery.conf.broker_transport_options = app.config['CELERY_BROKER_TRANSPORT_OPTIONS']
        # celery.conf.result_backend_transport_options = app.config['CELERY_BROKER_TRANSPORT_OPTIONS']
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
