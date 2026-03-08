import os
import json

from src.constants import level_dict_kor
from src.preprocess import preprocess

class Data:
    def __init__(self, dir: str = "data"):
        self.data_dir = dir
        if not os.path.exists(f'{dir}/hanja.json'):
            print("배정 한자 데이터 파일이 없습니다. 데이터를 생성합니다.")
            preprocess(dir)
        with open(f'{dir}/hanja.json', 'r', encoding='utf-8') as f:
            self.hanja_list = json.load(f)
