# -*- coding=utf-8 -*-
from time import sleep

from . import celery


@celery.task()
def exec_task(n1, n2):
    return n1 + n2


@celery.task()
def exec_task2(n1, n2):
    for i in range(100):
        print(i)
        sleep(5)
    return n1 + n2


@celery.task()
def kill_celery_task(task_id):
    celery.control.terminate(task_id)
