from typing import Callable, Dict
import config
from celery_tasks import celery_app
from celery_tasks.helpers import map_to_csvmodel, save_csv_file, post_url
from hub.one_word import get_caihongpi_info, get_acib_info, get_hitokoto_info, get_lovelive_info, get_wufazhuce_info

SITE: str = getattr(config, "SITE_URL")


def one_word_flow(func: Callable, file_path: str) -> Dict[str, str]:
    one_word = func
    info = one_word()
    model = map_to_csvmodel(info)
    path = file_path
    save_csv_file(path, model=model)
    return info


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def caihongpi():
    one_word = get_caihongpi_info
    path = './data/caihongpi.csv'

    word = one_word_flow(one_word, path)
    url: str = SITE + "/api/oneword/"
    json = {
        "content": word.get("content"),
    }
    rv = post_url(url, json=json)
    return rv.status_code == 200


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def acib():
    one_word = get_acib_info
    path = './data/acib.csv'

    word = one_word_flow(one_word, path)
    url: str = SITE + "/api/oneword/"
    json = {
        "content": word.get("content"),
        "translate": word.get("translation"),
        "picture": word.get("picture"),
    }
    rv = post_url(url, json=json)
    return rv.status_code == 200


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def hitokoto():
    one_word = get_hitokoto_info
    path = './data/hitokoto.csv'

    word = one_word_flow(one_word, path)
    url: str = SITE + "/api/oneword/"
    json = {
        "content": word.get("hitokoto"),
        "zuthor": word.get("from_who"),
    }
    rv = post_url(url, json=json)
    return rv.status_code == 200


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def lovelive():
    one_word = get_lovelive_info
    path = './data/lovelive.csv'

    word = one_word_flow(one_word, path)
    url: str = SITE + "/api/oneword/"
    json = {
        "content": word.get("content"),
    }
    rv = post_url(url, json=json)
    return rv.status_code == 200


@celery_app.task(default_retry_delay=300, max_retries=3, ignore_result=True)
def wufazhuce():
    one_word = get_wufazhuce_info
    path = './data/wufazhuce.csv'

    word = one_word_flow(one_word, path)
    url: str = SITE + "/api/oneword/"
    json = {"content": word.get("content"), "picture": word.get("image")}
    rv = post_url(url, json=json)
    return rv.status_code == 200
