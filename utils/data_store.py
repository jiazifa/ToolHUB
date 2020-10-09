import csv
import os
from typing import List, Any


def save_csv(file_path: str, headers: List[str], rows: List[List[Any]]):
    mode: str = 'w' if os.path.exists(file_path) else 'a+'

    with open(file_path, mode, newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
