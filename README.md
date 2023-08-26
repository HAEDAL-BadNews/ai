# Bad news - Ai😊
### HAEDAL_GROWTH_HACKATHON
<br>

## 주제
📰NLP기술을 이용한 관심 뉴스기사 요약
<br>
<br>

## 팀원 소개
| 권수현 | 권용민 | 김강민 | 김민주 | 
| :-----: | :-----: | :-----: | :-----: |
| [<img src="https://github.com/kwonssshyeon.png" width="100px">](https://github.com/kwonssshyeon) | [<img src="https://github.com/rnjs5540.png" width="100px">](https://github.com/rnjs5540) | [<img src="https://github.com/dobbymin.png" width="100px">](https://github.com/dobbymin) | [<img src="https://github.com/joojjang.png" width="100px">](https://github.com/joojjang) | 
| 백엔드 | 백엔드 | 프론트엔드 | 프론트엔드 | 
<br>

## 배포링크
> 백엔드 서버 : http://13.124.161.27:8080/
> <br>
> ai 서버 : http://15.165.122.3:8000/
> <br>
> 프론트엔드 서버 : 
<br>

## 프로젝트 주소
> 백엔드 : https://github.com/KNU-HAEDAL/BadNews-backend
> <br>
> ai : https://github.com/KNU-HAEDAL/BadNews-ai
> <br>
> 프론트엔드 : https://github.com/KNU-HAEDAL/BadNews-frontend
<br>


## 프로젝트 목적
이 서비스는 크게 2개의 목적이 있다.
<br>
요즘 사람들은 뉴스를 잘 보지 않는 경향이 있다.
<br>
집에 티비를 자주 본다면 자연스레 뉴스 기사들을 접할 수 있는 기회가 많지만, 직접 인터넷으로 찾아보지 않으면 접할 기회가 많이 없는 것이 사실이다.
<br>
이러한 문제를 해결하기 위해 뉴스기사를 실시간으로 가져와 사용자에 편하게 읽을 수 있게 정리하여 보여주도록 하는 것이 첫번째 목적이다.
<br>
두번째는 IT나 경제와 같이 변화의 속도가 빠른 분야에 대해 필요한 정보를 뒤쳐지지 않고 따라가는 것이 필요한 사람들이 있다.
<br>
이러한 사람들을 위해 더 편리하게 서비스를 제공받을 수 있도록 하는 것이 두번째 목적이다.
<br>
<br>


## 프로젝트 설명
<br>
<br>

## 프로젝트 구조
![프젝구조도](https://github.com/KNU-HAEDAL/BadNews-backend/assets/104684033/312c0981-5e49-41f5-9907-05a3842d3681)
<br>
<br>

## 개발기간
- 1차 : 2023.07.19 ~ 2023.07.22
- 2차 : 2023.08.16 ~
<br>
<br>

## 개발환경
Python : 3.11.1
<br>
Crome : 115.~
<details>
<summary>설치모듈☝️click!</summary>
<div markdown="1">       
aiohttp==3.8.5
<br>
aiosignal==1.3.1
<br>
annotated-types==0.5.0
<br>
anyio==3.7.1
<br>
async-timeout==4.0.3
<br>
attrs==23.1.0
<br>
beautifulsoup4==4.12.2
<br>
boto3==1.28.28
<br>
botocore==1.31.28
<br>
certifi==2023.7.22
<br>
cffi==1.15.1
<br>
charset-normalizer==3.2.0
<br>
click==8.1.6
<br>
colorama==0.4.6
<br>
exceptiongroup==1.1.3
<br>
fastapi==0.101.1
<br>
filelock==3.12.2
<br>
frozenlist==1.4.0
<br>
fsspec==2023.6.0
<br>
h11==0.14.0
<br>
huggingface-hub==0.16.4
<br>
idna==3.4
<br>
Jinja2==3.1.2
<br>
jmespath==1.0.1
<br>
MarkupSafe==2.1.3
<br>
mpmath==1.3.0
<br>
multidict==6.0.4
<br>
networkx==3.1
<br>
numpy==1.25.2
<br>
openai==0.27.8
<br>
outcome==1.2.0
<br>
packaging==23.1
<br>
protobuf==4.24.0
<br>
pycparser==2.21
<br>
pydantic==2.2.0
<br>
pydantic_core==2.6.0
<br>
PySocks==1.7.1
<br>
python-dateutil==2.8.2
<br>
python-dotenv==1.0.0
<br>
PyYAML==6.0.1
<br>
regex==2023.8.8
<br>
requests==2.31.0
<br>
s3transfer==0.6.2
<br>
safetensors==0.3.2
<br>
selenium==4.11.2
<br>
sentencepiece==0.1.99
<br>
six==1.16.0
<br>
sniffio==1.3.0
<br>
sortedcontainers==2.4.0
<br>
soupsieve==2.4.1
<br>
starlette==0.27.0
<br>
sympy==1.12
<br>
tokenizers==0.13.3
<br>
torch==2.0.1
<br>
tqdm==4.66.1
<br>
transformers==4.31.0
<br>
trio==0.22.2
<br>
trio-websocket==0.10.3
<br>
typing_extensions==4.7.1
<br>
urllib3==1.26.16
<br>
uvicorn==0.23.2
<br>
webdriver-manager==4.0.0
<br>
wsproto==1.2.0
<br>
yarl==1.9.2



</div>
</details>
  
<br>
<br>

## 로컬 실행방법
1.레포지토리 clone
<br>
`git clone https://github.com/KNU-HAEDAL/BadNews-ai.git`
<br>
<br>
2. 필요한 모듈설치
<br>
`pip install -r requirements.txt`
<br>
<br>
3. torch는 따로 설치
<br>
`pip install torch==1.25.2`
<br>
<br>
4. 실행
<br>
`uvicorn server_api:app --reload --port 8000`
<br>
&rarr; http://localhost:8000 으로 실행한다.
<br>
<br>

## branch 설명
- crawling : 뉴스기사 크롤링을 구현
- summary : 기사 요약을 구현
- image : 이미지 생성을 구현
- keyword : 키워드 추출 구현
- connect_server : 스프링 서버와 통신을 위한 API구현

