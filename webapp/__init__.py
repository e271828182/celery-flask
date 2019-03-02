from flask import Flask
# from celery_runner import make_celery
from celery import Celery


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(
        CELERY_BROKER_URL='redis://192.168.10.12:6379',
        CELERY_RESULT_BACKEND='redis://192.168.10.12:6379'
    )
    # celery = make_celery(flask_app)
    # celery.init_app(flask_app)

    return flask_app


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
