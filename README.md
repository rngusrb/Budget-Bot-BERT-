# 가계봇: AI 기반 스마트 가계부 시스템

BERT 모델을 활용한 문자 분류와 PyQt 기반 사용자 인터페이스를 결합한 개인화 소비 분석 및 절약 지원 프로그램입니다.

![가계봇 메인 이미지](https://github.com/user-attachments/assets/e499d249-03da-4a92-8a82-5fc8795c65b6)

---

## 프로젝트 목적

- 문자로 수신된 소비 내역을 자동 분류 및 저장
- 설정한 소비 한도 초과 시 경고 제공
- 공공 통계를 기반으로 절약 가능 분야와 금액을 사용자에게 제시

---

## 주요 기능

1. 문자 기반 소비 카테고리 분류
- 문자 내용을 BERT 기반 모델로 분석하여 소비 항목 분류
- 예: "GS25에서 5,000원 사용" → 편의점/마트 카테고리 분류
- 사전학습 모델을 파인튜닝하여 정확도 향상 (Test Accuracy 0.93)

![분류 결과 시각화](https://github.com/user-attachments/assets/0b50ab58-a3be-475c-a05e-7ce9f9fe745a)

2. 소비 한도 초과 알림
- 사용자가 입력한 월별 한도를 초과하는 경우 경고창 출력
- 카테고리별 한도 설정 가능

3. 소비 절약 추천 기능
- 사용자의 소비 기록을 KOSIS 통계와 비교
- 과소비 항목 파악 후 절약 가능한 항목 및 금액 계산
- 사용자 나이대의 평균 소비 대비 절약 필요 비율 계산

![소비 절약 기능 이미지](https://github.com/user-attachments/assets/4cfb5179-5af0-449c-9780-637a937fcad4)

---

## 사용 기술

1. BERT 기반 자연어 처리
- Transformers 라이브러리 사용
- KoBERT 모델을 분류용으로 파인튜닝
- 데이터 불균형 문제를 해결하기 위해 EDA 기법 적용

2. 데이터 증강 (EDA)
- Random Deletion 기법 사용: 단어를 무작위로 제거하여 새로운 학습 샘플 생성
- 주요 목표는 특정 레이블(예: 마트/편의점)의 데이터 보강

![데이터 증강 시각화](https://github.com/user-attachments/assets/0d8a9fbd-6b09-4498-8dde-560b99b0eed2)

3. GUI 프레임워크: PyQt5
- 소비 기록 입력, 분류 결과 출력, 알림창, 절약 추천 등 모든 동작을 GUI로 제공
- UI 파일들은 Qt Designer를 통해 제작하고 PyQt5로 로딩

![프레임워크 구성도](https://github.com/user-attachments/assets/6986b978-7e8a-4b4b-99fb-9805e95b90cd)

4. 데이터 저장
- 소비 기록, 분석 결과, 사용자 입력값 등을 txt 및 csv 파일로 저장 및 관리

---

## 디렉토리 구조 요약

```
.
├── main.py                 # 메인 실행 파일
├── bert_분류모델_2.py       # BERT 분류 모델 학습 및 추론
├── graph.py, fix.py 등     # 각 기능별 분리된 스크립트
├── save/                   # 소비 내역, 분류 결과 등 저장 파일들
├── ui/                     # PyQt UI 정의 파일 (.ui)
├── bert/config.json        # 모델 설정 파일
├── 최종.pptx                # 발표 자료
```

---

## 실행 방법

```
python main.py
```

GUI 창이 실행되며, 문자 입력 → 분류 → 절약 추천까지 전체 흐름이 지원됨

---

## 주요 화면 기능
- 문자 입력 창
- 소비 내역 분류 결과 시각화
- 설정된 한도 초과 시 경고창 팝업
- 절약 항목 및 금액 제안

---

## 성능 및 개선 사항
- 분류 정확도 93% 달성
- 오분류 문제 존재: 미학습 음식점 이름, 중의적 표현 등
- 개선 방향: 데이터셋 보강 및 하이퍼파라미터 최적화

---

## 개발자
- 구현규 외 1명 (GUI/분류기 담당 분담)

---

## 참고 자료
- Huggingface Transformers
- KoBERT 모델 및 KorQuAD 대회 자료
- 국가통계포털 (kosis.kr)
- Easy Data Augmentation (EDA)

