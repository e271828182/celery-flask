from flask import Flask
from webapp.task import celery


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


# def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_RESULT_BACKEND'],
#         broker=app.config['CELERY_BROKER_URL']
#     )
#     celery.conf.update(app.config)
#
#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery



