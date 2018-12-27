import requests
from celery import shared_task
from celery.utils.log import get_task_logger as getLogger
from django.conf import settings

logger = getLogger(__name__)

STUDENTS = settings.STUDENTS
UNVIERCITY = settings.UNIVERCITY


@shared_task(bind=True, retry_backoff=True, retry_kwargs={'max_retries': 6})
def delete_students(url):
    response = requests.post(f'{STUDENTS}/api/v1/portfolio/site_delete/?url={url}')


@shared_task(bind=True, retry_backoff=True, retry_kwargs={'max_retries': 6})
def delete_univercity(url):
    response = requests.post((f'{UNIVERCITY}/api/v1/orders/delete/?url={url}'))