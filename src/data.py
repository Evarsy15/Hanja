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

    def get_studied_hanja(self, iter: int, grade: int) -> list:
        if not hasattr(self, 'studied_hanja'):
            if iter == 1:
                self.studied_hanja = [hanja for hanja in self.hanja_list 
                                      if hanja['grade'] >= grade and hanja['selected']]
            elif iter > 1:
                self.studied_hanja = [hanja for hanja in self.hanja_list
                                      if hanja['grade'] >= grade]
            else:
                raise ValueError(
                    f"Data.get_studied_hanja(): Invalid iteration {iter}. "
                    f"(Expected `iter` >= 1)"
                )
        return self.studied_hanja
