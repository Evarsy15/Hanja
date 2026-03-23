import os
import ast
import json

from src.config import Config
from src.preprocess import preprocess

def format_hanja(hanja: dict) -> str:
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

def get_representative(hanja: dict) -> str:
    meaning_parse = ast.literal_eval(hanja['meaning'])
    rep_m = meaning_parse[0][0][0]  # 대표 의미
    rep_s = meaning_parse[0][1][0]  # 대표 음
    return f'{rep_m} {rep_s}'

def get_repr_pairs(hanja: dict) -> list[str]:
    meaning_parse = ast.literal_eval(hanja['meaning'])
    pairs = []
    for meaning in meaning_parse:
        _m = meaning[0]
        _s = meaning[1]; assert len(_s) == 1, "invalid format"
        for __m in _m:
            pairs.append(f'{__m} {_s[0]}')
    return pairs
