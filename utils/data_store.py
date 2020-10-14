import csv
import os
from typing import Dict, List, Any, Union


class CSVModel:
    def __init__(self, headers: List[str], rows: List[List[str]]):
        self._headers = headers
        self._rows = rows

    @classmethod
    def create_from_dict(cls, content: Dict[str, str]) -> 'CSVModel':
        return CSVModel(list(content.keys()), [list(content.values())])


def save_csv(file_path: str,
             headers: Union[List[str], None] = None,
             rows: Union[List[List[Any]], None] = None,
             model: Union[CSVModel, None] = None):

    ensure_folder_exists(file_path)
    is_exists: bool = True if os.path.exists(file_path) else False

    mode: str = 'a+' if is_exists else 'w'
    with open(file_path, mode, newline='') as f:
        f_csv = csv.writer(f)

        real_headers: List[str] = headers or model._headers if model else ['']
        real_rows: List[List[Any]] = rows or model._rows if model else [[]]

        if not is_exists:
            f_csv.writerow(real_headers)
        f_csv.writerows(real_rows)


def ensure_folder_exists(file_path: str):
    if os.path.exists(file_path):
        return

    folder: str = os.path.dirname(file_path)

    if os.path.exists(folder):
        return

    os.mkdir(folder)
