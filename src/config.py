import json

from src.constants import level_dict_kor

class Config:
    def __init__(self, path: str = "config.json"):
        self.path = path
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.load_config(f)
        except FileNotFoundError:
            print("설정 파일이 없습니다. 초기 설정을 진행합니다.")
            print("-"*40)
            self.create_config()

    def create_config(self):
        while True:
            grade = input("몇 급을 공부하시겠어요? : ")
            if grade in level_dict_kor:
                self.grade = level_dict_kor[grade]
                break
            else:
                print("잘못된 급수입니다.")
        while True:
            num_hanja = input("한자 추첨 시 한 번에 고를 한자 수를 입력해주세요. : ")
            if num_hanja.isdigit() and int(num_hanja) > 0:
                self.num_hanja = int(num_hanja)
                break
            else:
                print("잘못된 입력입니다. 양의 정수를 입력해주세요.")
        self.strike = 0
        self.last_login = ""
        self.iteration = 1
        self.save_config()

    def load_config(self, f):
        data = json.load(f)

        self.grade = data.get('grade', 12)           # 목표 한자 급수
        self.num_hanja = data.get('num_hanja', 5)    # 한자 추첨 시 선택할 한자 수
        self.strike = data.get('strike', 0)          # 연속 출석 일수
        self.last_login = data.get('last_login', "") # 마지막 로그인 날짜 (YYYY-MM-DD)
        self.iteration = data.get('iteration', 1)    # 한자 급수 순회 횟수

        self.hanja_list = []  # 한자 데이터는 별도로 로드

    def save_config(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump({
                "grade": self.grade,
                "num_hanja": self.num_hanja,
                "strike": self.strike,
                "last_login": self.last_login,
                "iteration": self.iteration
            }, f, ensure_ascii=False, indent=4)

def change_config(config: Config):
    while True:
        print("-"*40)
        print("설정 변경:")
        print(" 1. 급수 변경")
        print(" 2. 한자 추첨 수 변경")
        print(" 3. 나가기")

        choice = input(">> ")
        match choice:
            case "1":
                while True:
                    print("-"*40)
                    grade = input("몇 급을 공부하시겠어요? : ")
                    if grade in level_dict_kor:
                        config.grade = level_dict_kor[grade]
                        break
                    else:
                        print("잘못된 급수입니다.")
            case "2":
                while True:
                    print("-"*40)
                    num_hanja = input("한자 추첨 시 한 번에 고를 한자 수를 입력해주세요. : ")
                    if num_hanja.isdigit() and int(num_hanja) > 0:
                        config.num_hanja = int(num_hanja)
                        break
                    else:
                        print("잘못된 입력입니다. 양의 정수를 입력해주세요.")
            case "3":
                print("-"*40)
                print("설정 변경을 종료합니다.")
                break
            case _:
                print("-"*40)
                print("잘못된 입력입니다. 다시 시도해주세요.")
