import requests
from typing import Union
from utils import get_logger

logger = get_logger(__name__)


def get_caihongpi_info() -> Union[str, None]:
    url: str = 'https://chp.shadiao.app/api.php'
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return None
        content: str = resp.text
        return content
    except requests.exceptions.RequestException as exception:
        logger.debug(exception)
        return None
