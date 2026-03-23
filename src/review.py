import os
import json
import random

from src.auxiliary import format_hanja, get_repr_pairs_user
from src.config import Config
from src.data import Data

def review_hanja(config: Config, data: Data):
    studied_hanja = data.get_studied_hanja(config.iteration, config.grade)
    while True:
        cand = random.choice(studied_hanja)
        print("-"*40)
        print(f"다음 한자의 훈음은?")
        print(f" {cand['hanja']}")
        
        ans = input(" > ")
        if ans in get_repr_pairs_user(cand):
            print("정답! ", end='')
            print(f"{format_hanja(cand)}")
        else:
            print("틀렸습니다. 정답은 다음과 같습니다. ", end='')
            print(f"{format_hanja(cand)}")
        
        print("-"*40)
        again = input("다시 하시겠습니까? (y/n) > ")
        if again.lower() == 'n':
            print("복습을 종료합니다.")
            break
