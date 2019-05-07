# -*- coding=utf-8 -*-
from flask import Flask


def register_web_blueprint(app):
    from webapp.controller import controller
    from webapp.ws import ws
    app.register_blueprint(controller)
    app.register_blueprint(ws)


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(
        BROKER_URL='sentinel://:%(password)s@%(node1)s;sentinel://:%(password)s@%(node2)s;sentinel://:%(password)s@%(node3)s' % {
            'password': 'wIvJt@_redis',
            'node1': '192.168.11.29:26001',
            'node2': '192.168.11.32:26001',
            'node3': '192.168.11.20:26001'
        },
        CELERY_RESULT_BACKEND='sentinel://:%(password)s@%(node1)s;sentinel://:%(password)s@%(node2)s;sentinel://:%(password)s@%(node3)s' % {
            'password': 'wIvJt@_redis',
            'node1': '192.168.11.29:26001',
            'node2': '192.168.11.32:26001',
            'node3': '192.168.11.20:26001'
        },
        BROKER_TRANSPORT_OPTIONS={
            'master_name': "master-dev"
        },
        CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS={
            'master_name': "master-dev"
        }
    )

    from webapp.task import make_celery
    make_celery(flask_app)

    from webapp.ws import socketio
    socketio.init_app(flask_app)

    register_web_blueprint(flask_app)

    return flask_app, socketio



