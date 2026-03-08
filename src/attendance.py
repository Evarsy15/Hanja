import os
from src.config import Config
from datetime import datetime

def update_attendance(config: Config):
    today = datetime.now().date()
    if config.last_login:
        last_login_date = datetime.strptime(config.last_login, "%Y-%m-%d").date()
        diff = (today - last_login_date).days
        if diff == 1:
            config.strike += 1
            print(f"오늘은 연속 출석 {config.strike}일차!")
        elif diff > 1:
            config.strike = 1
            print(f"출석이 끊겼어요. (마지막 로그인: {config.last_login})")
        elif diff == 0:
            pass
        else:
            print("날짜 오류: 마지막 로그인 날짜가 미래입니다. 출석 기록을 초기화합니다.")
            config.strike = 1
        config.last_login = today.strftime("%Y-%m-%d")
    else:
        config.strike = 1
        config.last_login = today.strftime("%Y-%m-%d")
        print("첫 출석입니다!")
