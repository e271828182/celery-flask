from flask import Flask


def register_web_blueprint(app):
    from webapp.controller import controller
    from webapp.ws import ws_c
    app.register_blueprint(controller)
    app.register_blueprint(ws_c)


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(
        CELERY_BROKER_URL='redis://192.168.10.12:6379/1',
        CELERY_RESULT_BACKEND='redis://192.168.10.12:6379/2'
    )

    from webapp.task import make_celery
    make_celery(flask_app)

    from webapp.ws import ws
    ws.init_app(flask_app)

    register_web_blueprint(flask_app)

    return flask_app, ws



