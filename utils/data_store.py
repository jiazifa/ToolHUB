import csv
import os
from typing import List, Any, Union


class CSVModel:
    def __init__(self, headers: List[str], rows: List[List[str]]):
        self._headers = headers
        self._rows = rows


def save_csv(file_path: str,
             headers: Union[List[str], None] = None,
             rows: Union[List[List[Any]], None] = None,
             model: Union[CSVModel, None] = None):
    is_exists: bool = True if os.path.exists(file_path) else False

    mode: str = 'a+' if is_exists else 'w'
    with open(file_path, mode, newline='') as f:
        f_csv = csv.writer(f)

        real_headers = headers or model._headers
        real_rows = rows or model._rows

        if not is_exists:
            f_csv.writerow(real_headers)
        f_csv.writerows(real_rows)
