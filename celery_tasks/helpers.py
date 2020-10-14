from typing import Dict
import utils
from celery_tasks import celery_app

__all__ = ['map_to_csvmodel', 'save_csv_file']


@celery_app.task
def map_to_csvmodel(content: Dict[str, str]) -> utils.CSVModel:
    return utils.CSVModel.create_from_dict(content)


@celery_app.task()
def save_csv_file(file_path: str, model: utils.CSVModel):
    utils.save_csv(file_path, model=model)
