from utils import save_csv, CSVModel
import os

def test_zhihu_rss():
    from hub.rss import parser_feed, parse_inner
    rss = parser_feed
    url = "https://www.zhihu.com/rss"
    
    content = parser_feed(url)
    result = parse_inner(url, content)
    assert result
    path = "./data/test_zhihu.csv"
    for r in result:
        model: CSVModel = CSVModel.create_from_dict(r)
        save_csv(path, model=model)
    
    assert os.path.exists(path)
