# from celery_flask import celery
from webapp import make_celery
from flask import current_app


celery = make_celery(current_app._get_current_object)


@celery.task()
def exec_task(n1, n2):
    return n1 + n2