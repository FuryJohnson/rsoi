from .base import *

try:
    from .local import *
except ImportError:
    pass

from conf.celeryconfig import app as celery_app

__all__ = ['celery_app']