from flask import Flask


def register_web_blueprint(app):
    from webapp.controller import controller
    app.register_blueprint(controller)


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(
        CELERY_BROKER_URL='redis://192.168.10.12:6379/1',
        CELERY_RESULT_BACKEND='redis://192.168.10.12:6379/2'
    )

    from webapp.task import make_celery
    make_celery(flask_app)

    register_web_blueprint(flask_app)

    return flask_app



