from lxml import etree
from typing import Union


def parser_first_text_or_content_if_could(html: etree._Element,
                                          query_path: str) -> Union[str, None]:
    """
    如果解析出的内容是一个数组，默认取的第一个
    """
    nodes = html.xpath(query_path)
    if not nodes:
        return None

    if len(nodes) > 0:
        desc = nodes[0]
        if hasattr(desc, 'text'):
            return str(desc.text)
        return str(desc)

    return None
