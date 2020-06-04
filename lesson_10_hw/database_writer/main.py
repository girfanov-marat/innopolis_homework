"""Файл для запуска."""
import json

from lesson_10_hw.database_writer import database_processing as ds
from lesson_10_hw.database_writer import json_processing as jp

my_file = 'example.json'

with open(my_file, encoding="utf-8") as f:
    json_content = json.load(f)

if __name__ == "__main__":
    if jp.validate_json(json_content):
        ds.create_tables()
        ds.insert_or_update(jp.dict_parser(json_content))
    else:
        print("Не валидный JSON")
