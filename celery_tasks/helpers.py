from typing import Dict, Union, Any
import requests
from requests import Response
import utils
from celery_tasks import celery_app

__all__ = ['map_to_csvmodel', 'save_csv_file']


@celery_app.task
def map_to_csvmodel(content: Dict[str, str]) -> utils.CSVModel:
    return utils.CSVModel.create_from_dict(content)


@celery_app.task
def save_csv_file(file_path: str, model: utils.CSVModel):
    utils.save_csv(file_path, model=model)


@celery_app.task
def post_url(url: str,
             data: Union[Any, None] = None,
             json: Union[Dict[str, str], None] = None,
             **kwargs) -> Response:
    return requests.post(url, data=data, json=json, **kwargs)


@celery_app.task
def get_url(url: str, params: dict, **kwargs) -> Response:
    return requests.get(url, params=params, **kwargs)
