from flask import Flask
from celery_runner import make_celery


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(
        CELERY_BROKER_URL='redis://192.168.10.12:6379',
        CELERY_RESULT_BACKEND='redis://192.168.10.12:6379'
    )
    celery = make_celery(flask_app)
    celery.init_app(flask_app)

    return flask_app, celery
