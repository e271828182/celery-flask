from webapp import create_app
from webapp.task import make_celery


flask_app = create_app()
celery = make_celery(flask_app)

