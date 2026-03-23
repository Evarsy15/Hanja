import os
from datetime import datetime

from src.attendance import update_attendance
from src.config import Config, change_config
from src.data import Data
from src.review import review_hanja
from src.select import select_random_hanja

def menu_study(config: Config, data: Data):
    print("-"*40)
    print("무엇을 공부하시겠어요?")
    print(" 1. 랜덤 한자 추첨")
    print(" 2. 배운 한자 복습")
    print(" 3. 사자성어 공부")
    print(" 4. 반대자/반대어")
    print(" 5. 유의자/유의어")
    print(" 6. 나가기")

    choice = input(">> ")
    match choice:
        case "1":
            select_random_hanja(config, data)
        case "2":
            review_hanja(config, data)
        case "3":
            print("사자성어 공부 기능은 아직 구현되지 않았습니다.")
        case "4":
            print("반대자/반대어 기능은 아직 구현되지 않았습니다.")
        case "5":
            print("유의자/유의어 기능은 아직 구현되지 않았습니다.")
        case "6":
            print("공부 메뉴를 종료합니다.")
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요.")

def menu_info(config: Config, data: Data):
    print("-"*40)
    print("내 정보:")
    print(f" - 연속 출석 일수: {config.strike}일")
    print(f" - 마지막 로그인 날짜: {config.last_login}")
    print(f" - 지금까지 고른 한자 수: {sum(1 for h in data.hanja_list if h['selected'])}개")

# 최상위 메뉴
def menu_top(config: Config, data: Data):
    while True:
        print("-"*40)
        print("메뉴를 선택해주세요:")
        print(" 1. 한자 공부하기")
        print(" 2. 내 정보")
        print(" 3. 설정 변경")
        print(" 4. 프로그램 종료")

        choice = input(">> ")
        match choice:
            case "1": # 한자 공부하기
                menu_study(config, data)
            case "2": # 내 정보
                menu_info(config, data)
            case "3": # 설정 변경
                change_config(config)
            case "4": # 프로그램 종료
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못된 입력입니다. 다시 시도해주세요.")
        

    # 프로그램 종료 전 설정 저장
    config.save_config()

def main():
    os.makedirs("data", exist_ok=True)
    config = Config("config.json")

    print("-"*40)
    print(">> 한자 공부 프로그램 <<")
    print("-"*40)

    update_attendance(config)

    print("한자 데이터 로딩중...")
    data = Data("data")
    print("한자 데이터 로딩 완료!")

    menu_top(config, data)

if __name__ == "__main__":
    main()
