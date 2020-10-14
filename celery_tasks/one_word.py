from typing import Callable
from celery_tasks import celery_app
from celery_tasks.helpers import map_to_csvmodel, save_csv_file
from hub.one_word import get_caihongpi_info, get_acib_info, get_hitokoto_info, get_lovelive_info, get_wufazhuce_info


def one_word_flow(func: Callable, file_path: str):
    one_word = func
    info = one_word()
    model = map_to_csvmodel(info)
    path = file_path
    save_csv_file(path, model=model)


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def caihongpi():
    one_word = get_caihongpi_info
    path = './data/caihongpi.csv'
    one_word_flow(one_word, path)


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def acib():
    one_word = get_acib_info
    path = './data/acib.csv'
    one_word_flow(one_word, path)


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def hitokoto():
    one_word = get_hitokoto_info
    path = './data/hitokoto.csv'
    one_word_flow(one_word, path)


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def lovelive():
    one_word = get_lovelive_info
    path = './data/lovelive.csv'
    one_word_flow(one_word, path)


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def wufazhuce():
    one_word = get_wufazhuce_info
    path = './data/wufazhuce.csv'
    one_word_flow(one_word, path)
