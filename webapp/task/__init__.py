from celery import Celery

celery = Celery()


def make_celery(app):
    # celery = Celery(
    #     app.import_name,
    #     backend=app.config['CELERY_RESULT_BACKEND'],
    #     broker=app.config['CELERY_BROKER_URL']
    # )
    celery.main = app.import_name
    # celery.__autoset('result_backend', app.config['CELERY_RESULT_BACKEND'])
    # celery.__autoset('broker_url', app.config['CELERY_BROKER_URL'])

    # celery.backend = app.config['CELERY_RESULT_BACKEND']
    # celery.broker_connection = app.config['CELERY_BROKER_URL']
    #
    # celery.conf.update(app.config)

    celery.conf.update(
        CELERY_RESULT_BACKEND=app.config['CELERY_RESULT_BACKEND'],
        CELERY_BROKER_URL=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
