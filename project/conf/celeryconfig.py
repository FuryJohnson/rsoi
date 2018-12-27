import os

# import environ

# ROOT_DIR = environ.Path(__file__) - 2
# broker_url ='amqp://localhost'


from celery import Celery
from celery import signals
from celery.utils.log import get_task_logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
logger = get_task_logger(__name__)

from django.conf import settings

app = Celery('base_me', broker='pyamqp://guest@localhost//')
# app.conf.timezone = 'Europe/Moscow' use from config
# app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content

    timezone='Europe/Moscow',
    enable_utc=True,
    broker_pool_limit=1,  # Will decrease connection usage
    broker_heartbeat=None,  # We're using TCP keep-alive instead
    broker_connection_timeout=30,  # May require a long timeout due to Linux DNS timeouts etc
    result_backend=None,  # AMQP is not recommended as result backend as it creates thousands of queues
    event_queue_expires=60,  # Will delete all celeryev. queues without consumers after 1 minute.
    worker_prefetch_multiplier=1,  # Disable prefetching, it's causes problems and doesn't help performance
    worker_concurrency=50,
    # If you tasks are CPU bound, then limit to the number of cores, otherwise increase substainally
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# logger = logging.getLogger(__name__)
# Celery > 4.0 tries to configure logging
# and very often breaks the configuration.
# See: https://github.com/celery/celery/issues/2437
# Need to set `CELERYD_HIJACK_ROOT_LOGGER = False`
# in django settings.py and enable the following signal
@signals.setup_logging.connect
def setup_logging(**kwargs):
    """Setup logging."""
    pass