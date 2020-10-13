from celery import Celery
import config

celery_app = Celery(__name__)
celery_app.conf.update(config)
