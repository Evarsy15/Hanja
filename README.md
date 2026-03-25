# 한자 공부 프레임워크 (개인용)

사단법인 한국어문회 주관 한국한자능력검정회 시행 전국한자능력검정시험을 위한 한자 공부 프로그램입니다.

※ 기본 내장된 배정 한자 데이터의 저작권은 한국어문회에 있습니다. 또한, 배정 한자를 제외한 자료(사자성어, 유의어/반대어, 동음이의어 등)의 경우 본 저장소에서는 프로그램에서 사용하는 JSON format만 공개합니다. 내용은 교재를 구매하여 `data/` 디렉토리에 채워넣으시기 바랍니다. [교재 구매하기: https://skymiru.co.kr/]

※ 본 저장소는 한국어 전용으로만 작성되어 있습니다. This repository supports only Korean.

※ 개인용 프로젝트로, 설계는 직접 하고 코드는 GitHub Copilot / Gemini 등 생성형 AI의 도움을 받아 작성하였습니다.

## 설치하기

본 프로그램을 실행하기 위해 필요한 패키지 목록은 다음과 같습니다.

```bash
# 필수 요구사항
Python >= 3.10

# GUI 관련 요구사항
PyQt6
CnOCR
```

본 저장소는 다음과 같이 로컬에 설치할 수 있습니다.

```bash
git clone --recursive https://github.com/Evarsy15/Hanja.git

or

git clone https://github.com/Evarsy15/Hanja.git
cd Hanja
git submodule update --init --recursive
```

GUI 전용 추가 패키지는 `pip install`을 통해 설치할 수 있습니다. 또는, 해당 저장소를 복제한 뒤 아래 스크립트로 가상환경 생성 + 의존성 설치를 한 번에 실행할 수 있습니다.

```bash
python setup_env.py
```

현재 활성화된 파이썬 환경에 바로 설치하려면 아래처럼 실행하세요:

```bash
python setup_env.py --no-venv
```

## 사용하기

본 프로그램은 100% Python으로 작성되어 있습니다. 프로젝트 루트에서 Python으로 메인 파일을 실행하면 됩니다.

```bash
# CLI Main
python3 cli_main.py

# GUI Main
python3 gui_main.py
```

## 업데이트 내용

**2026. 03. 24** - 이미 추첨된 한자의 훈음을 복습하는 기능이 추가되었습니다.

**2026. 03. 08** - 한자 랜덤 추첨기가 적용되었습니다.

---

<div align="center">
Developed by Nix (rabbitnix @ postech.ac.kr)
</div>
