import time
from typing import Union, Dict, Any, List
import requests
import feedparser
from utils import get_unix_time_tuple, get_logger, filter_all_img_src


logger = get_logger(__name__)


def parser_feed(feed_url: str) -> Dict[str, Any]:
    feeds = feedparser.parse(feed_url)
    payload: Dict[str, Any] = {}
    if not hasattr(feeds, 'version'):
        return payload
    version = feeds.version
    title = feeds.feed.title if hasattr(feeds.feed, 'title') else ''  # rss的标题
    link = feeds.feed.link if hasattr(feeds.feed, 'link') else None  # 链接
    if not link:
        return payload

    payload['version'] = version
    payload['title'] = title
    payload['link'] = link
    subtitle = None
    if version == 'atom10':
        subtitle = ''
    elif version == 'rss20':
        subtitle = feeds.feed.subtitle or ''  # 子标题
    payload['subtitle'] = subtitle

    result = []
    for item in feeds['entries']:
        r = {}
        for k in item:
            r[k] = item[k]
        result.append(r)
    payload['items'] = result
    return payload


def parse_inner(url: str, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []

    if not payload:
        return result
    if len(payload) == 0:
        return result
    operator_map = {
        "rss20": parse_rss20,
        "atom10": parse_atom,
        "rss10": parse_rss10,
    }
    operator = operator_map.get(payload["version"]) or parse_rss20
    if not operator:
        return result
    version = payload['version'] if hasattr(payload, 'version') else ''
    title = payload['title'] or '无标题'
    subtitle = payload['subtitle']
    items = payload['items']
    
    for item in items:
        try:
            parsed = operator(item)
            if not parsed:
                continue
            descript = ""
            title = parsed.get('title') or ''
            link = parsed.get('link') or ''
            cover_img = parsed.get('cover_img') or ''
            published = parsed.get('published') or ''
            descript = parsed.get('descript') or ''
            parsed.setdefault('site', url)
            timeLocal = get_unix_time_tuple()
            # TODO: 写入数据
            result.append(parsed)
        except Exception as error:
            print(error)
            continue
    
    return result


def parse_rss20(item: Dict[str, Any]) -> Union[None, Dict[str, Any]]:
    """ 
    知乎订阅解析
    {
        "title": "",
        "title_detail": {"type": "text/plain", "language": null, "base": "https://www.zhihu.com/rss", "value": "《彩虹六号：围攻》咖啡厅关卡探讨空间类型组构"},
        "links": [{"rel": "alternate", "type": "text/html", "href": "http://zhuanlan.zhihu.com/p/75380766?utm_campaign=rss&utm_medium=rss&utm_source=rss&utm_content=title"}]
        "link": "",
        "summary": "<>",
        "summary_detail": {"type": "text/html", "language": null, "base": "https://www.zhihu.com/rss", "value": "<>"},
        "authors": [{"name": "暴走的巫師"}],
        "author": "暴走的巫師", 
        "author_detail": {"name": "暴走的巫師"}, 
        "published": "Thu, 01 Aug 2019 19:30:36 +0800", 
        "published_parsed": 12334323423, 
        "id": "http://zhuanlan.zhihu.com/p/75380766", 
        "guidislink": false
    }
    """
    try:
        result: Dict[str, Any] = {}
        title: str = item["title"]
        summary: str = item["summary"]
        imgs = filter_all_img_src(summary)
        link: str = item["link"] or item["id"] or ""
        published = time.gmtime(time.time())
        
        if hasattr(item, "published"):
            published = item["published"]
        if hasattr(item, "published_parsed"):
            published = item["published_parsed"]

        published = str(time.mktime(published))
        result.setdefault("title", title)
        result.setdefault("descript", summary)
        result.setdefault("link", link)
        if len(imgs) > 0:
            result.setdefault("cover_img", imgs[0])
        result.setdefault('published', published)
        return result
    except Exception as error:
        print(str(error))
        return None


def parse_rss10(item: Dict[str, Any]) -> Union[Dict[str, Any], None]:
    return parse_rss20(item)


def parse_atom(item: Dict[str, Any]) -> Union[Dict[str, Any], None]:
    return parse_rss20(item)