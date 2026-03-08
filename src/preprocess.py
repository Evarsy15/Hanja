import csv
import json

from src.constants import level_dict_kor

def preprocess(data_dir: str = "data"):
    with open('hanja_dataset/hanja.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # 필드 추가 및 초기값 설정
    for item in data:
        item['grade'] = level_dict_kor[item['level']]
        item['selected'] = False  # 초기값 설정

    with open(f'{data_dir}/hanja.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
