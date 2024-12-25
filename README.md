# 가계봇
![image](https://github.com/user-attachments/assets/e499d249-03da-4a92-8a82-5fc8795c65b6)

## framework QT
![image](https://github.com/user-attachments/assets/6986b978-7e8a-4b4b-99fb-9805e95b90cd)


## BERT 언어 모델을 통한 문자 분류
![image](https://github.com/user-attachments/assets/0b50ab58-a3be-475c-a05e-7ce9f9fe745a)
>pre train 모델을 이용하여 문자 내용에 따라 카테고리 분류하도로 튜닝

`from transformers import BertTokenizer`

`from transformers import BertForSequenceClassification, AdamW, BertConfig`

>하이퍼 파라미터 튜닝


`optimizer = AdamW(model.parameters(),
                  lr = 2e-5, # 학습률
                  eps = 1e-8 # 0으로 나누는 것을 방지하기 위한 epsilon 값
                )`

`epochs = 8`

### 데이터 증강 기술
-데이터 불균형 발생
![image](https://github.com/user-attachments/assets/0d8a9fbd-6b09-4498-8dde-560b99b0eed2)

 최종 모델의 Test Accuracy: 0.93



## 기타 기능
### 한도 비용 설정
### 소비 절약 기능
![image](https://github.com/user-attachments/assets/4cfb5179-5af0-449c-9780-637a937fcad4)
