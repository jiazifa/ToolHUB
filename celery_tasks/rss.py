from typing import List, Dict, Any
from celery_tasks import celery_app
from celery_tasks.helpers import map_to_csvmodel, save_csv_file
from hub.rss import parse_inner, parser_feed
from utils import save_csv, CSVModel, get_domain

@celery_app.task(default_retry_delay=3000, max_retries=3, ignore_result=True)
def parse_rsses():
    from config import RSS_SOUECES
    sources = RSS_SOUECES
    rsses_result: List[CSVModel] = []
    
    for url in sources:
        path: str = './data/' + get_domain(url) + '.csv'
        result = parser_feed(url)
        r_list = parse_inner(url, result)
        rsses_result.extend(r_list)
        for d in rsses_result:
            model = CSVModel.create_from_dict(d)
            save_csv(path, model=model)
        