from webapp import create_app
from webapp import make_celery


flask_app = create_app()
celery = make_celery(flask_app)

