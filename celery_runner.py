# -*- coding=utf-8 -*-
from webapp import create_app
from webapp.task import make_celery


flask_app, _ = create_app()
celery = make_celery(flask_app)

