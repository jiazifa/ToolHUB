from celery_tasks import celery_app
import config

celery_app.config_from_object(config)

app = celery_app
