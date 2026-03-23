import os
import ast
import json
import random
from datetime import datetime
from src.config import Config
from src.data import Data
from src.preprocess import preprocess

def format_hanja(hanja):
    meaning_parse = ast.literal_eval(hanja['meaning'])
    fmt = f'{hanja["hanja"]} : '
    for meaning in meaning_parse:
        _m = meaning[0]
        _s = meaning[1]; assert len(_s) == 1, "invalid format"
        for __m in _m:
            fmt += f'{__m} {_s[0]} | '
    fmt = fmt[:-3]  # Remove the last " | "
    fmt += f' [{hanja["level"]}, 부수: {hanja["radical"]}, 총 획수: {hanja["total_strokes"]}]'
    return fmt

def select_random_hanja(config: Config, data: Data):
    print("-"*40)
    eligible_hanja = [h for h in data.hanja_list if int(h['grade']) >= config.grade and not h['selected']]

    if not eligible_hanja:
        print("이미 모든 한자를 골랐습니다. 한자 데이터를 초기화합니다.")
        for h in data.hanja_list:
            h['selected'] = False
        with open(f'{data.data_dir}/hanja.json', 'w', encoding='utf-8') as f:
            json.dump(data.hanja_list, f, ensure_ascii=False, indent=2)
        return None

    while True:
        selected_hanja = random.sample(eligible_hanja, min(config.num_hanja, len(eligible_hanja)))
        print("오늘의 한자는...")
        for i, hanja in enumerate(selected_hanja, 1):
            print(f'{i}. {format_hanja(hanja)}')
        print("입니다!")
        print("-"*40)
        print("이걸로 하시겠어요? : ", end="")
        ans = input().lower()
        if ans in ['y', 'yes', '네', '응']:
            for h in selected_hanja:
                h['selected'] = True
            with open(f'{data.data_dir}/hanja.json', 'w', encoding='utf-8') as f:
                json.dump(data.hanja_list, f, ensure_ascii=False, indent=2)
            return
        elif ans in ['q', 'quit', '종료']:
            print("추첨을 종료합니다.")
            print("-"*40)
            return
        else:
            print("다시 추첨합니다...")
            print("-"*40)
