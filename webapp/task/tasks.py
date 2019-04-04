# -*- coding=utf-8 -*-
from . import celery


@celery.task()
def exec_task(n1, n2):
    return n1 + n2