import time
from celery import shared_task

@shared_task
def testing_task(a,b):
    # "write your process code"
    
    time.sleep(5)
    # print('finish')
    c=a+b
    return c
