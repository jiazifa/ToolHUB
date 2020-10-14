import requests
from typing import Union, Dict, Any
import utils
from lxml import etree

logger = utils.get_logger(__name__)


def ensure_dict(content: Any) -> Dict[str, Any]:
    if not content:
        return {}
    elif isinstance(content, dict):
        return content
    else:
        return {'content': content}


def get_caihongpi_info() -> Union[Dict[str, str], None]:
    """
    从彩虹屁获得信息
    url:: https://chp.shadiao.app/api.php
    :return: 彩虹屁
    """
    url: str = 'https://chp.shadiao.app/api.php'
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return None
        content: str = resp.text
        return ensure_dict(content)
    except requests.exceptions.RequestException as exception:
        logger.debug(exception)
        return None


def get_acib_info() -> Union[Dict[str, str], None]:
    """
    从爱词霸获得信息
    """
    try:
        url: str = 'http://open.iciba.com/dsapi'
        resp = requests.get(url)
        if resp.status_code != 200:
            return None

        content_dict = resp.json()
        return content_dict

    except requests.exceptions.RequestException as exception:
        logger.debug(exception)
        return None


def get_hitokoto_info() -> Union[Dict[str, str], None]:
    """
    从『一言』获取信息。(官网：https://hitokoto.cn/)
    :return: str,一言。
    """
    try:
        url: str = 'https://v1.hitokoto.cn/'
        params: Dict[str, str] = {'encode': 'json'}
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            return None
        result = resp.json()
        return result
    except requests.exceptions.RequestException as exception:
        logger.debug(exception)
        return None


def get_lovelive_info() -> Union[Dict[str, str], None]:
    """
    从土味情话中获取信息
    """
    try:
        url: str = 'https://api.lovelive.tools/api/SweetNothings'
        resp = requests.get(url)
        if resp.status_code != 200:
            return None
        return ensure_dict(resp.text)

    except requests.exceptions.RequestException as exception:
        logger.debug(exception)
        return None


def get_wufazhuce_info() -> Union[Dict[str, str], None]:
    """
    http://wufazhuce.com/
    """
    user_url = 'http://wufazhuce.com/'
    try:
        resp = requests.get(user_url, headers=utils.get_header())
        if resp.status_code != 200:
            return None
        html = etree.HTML(resp.text)
        result: Dict[str, str] = {}

        if content := utils.parser_first_text_or_content_if_could(
                html, '//*[@id="carousel-one"]/div/div[1]/div[2]/div[2]/a'):
            result.setdefault('content', content)

        if image := utils.parser_first_text_or_content_if_could(
                html, '//*[@id="carousel-one"]/div/div[1]/a/img/@src'):
            result.setdefault('image', image)

        return result

    except Exception as exception:
        logger.debug(str(exception))
        return None
