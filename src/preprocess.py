import ast
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
        item['selected_ever'] = False  # 초기값 설정

        meaning_parse = ast.literal_eval(item['meaning'])
        meaning_user_parse = []; required = False
        for meaning in meaning_parse:
            _m = meaning[0]
            _s = meaning[1]; assert len(_s) == 1, "invalid format"

            meaning_user_parse.append([[], _s])
            for __m in _m:
                # 어문회 제공 훈에 식별을 위해 한자 서술을 포함하는 경우,
                # 이를 제거한 '사용자가 쉽게 입력할 수 있는' 형태의 훈음-의미 쌍을 생성
                # ex) "성(姓) 강 姜" -> "성 강 姜"
                # ex) "일[首荷] 대 戴" -> "일 대 戴"
                if __m.endswith(']'):
                    ___m = __m.split('[')[0]
                    meaning_user_parse[-1][0].append(___m)
                    required = True
                elif __m.endswith(')'):
                    ___m = __m.split('(')[0]
                    meaning_user_parse[-1][0].append(___m)
                    required = True
                else:
                    meaning_user_parse[-1][0].append(__m)
        if required:
            item['meaning_user'] = str(meaning_user_parse)

    with open(f'{data_dir}/hanja.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
