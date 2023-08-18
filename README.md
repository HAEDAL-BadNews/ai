# ai
### HAEDAL_GROWTH_HACKATHON
<br>
<br>

## 프로젝트 명
### Bad News
<br>

## 주제
NLP기술을 이용한 관심 뉴스기사 요약
<br>
<br>


## 목적
이 서비스는 크게 2개의 목적이 있다.
요즘 사람들은 뉴스를 잘 보지 않는 경향이 있다.
집에 티비를 자주 본다면 자연스레 뉴스 기사들을 접할 수 있는 기회가 많지만, 직접 인터넷으로 찾아보지 않으면 접할 기회가 많이 없는 것이 사실이다.
이러한 문제를 해결하기 위해 뉴스기사를 실시간으로 가져와 사용자에 편하게 읽을 수 있게 정리하여 보여주도록 하는 것이 첫번째 목적이다.
두번째는 IT나 경제와 같이 변화의 속도가 빠른 분야에 대해 필요한 정보를 뒤쳐지지 않고 따라가는 것이 필요한 사람들이 있다.
이러한 사람들을 위해 더 편리하게 서비스를 제공받을 수 있도록 하는 것이 두번째 목적이다.
<br>
<br>

## 프로젝트 구조
![전체구조](https://github.com/HAEDAL-BadNews/backend/assets/104684033/8f7f597f-b46f-4b89-a40d-6b94a7b77329)


## 실행방법
`uvicorn server_api:app --reload --port 5000`
<br>
<br>
**크롬버전:115.~~~에서 실행**
<br>
<br>

## 설치모듈
- transformers[sentencepiece]
- requests
- BeatifulSoup
- boto3

더 많이 있는데 나중에..적겠음..
<br>

## branch 설명
- **crawling :** 뉴스기사 크롤링을 구현
- **summary :** 기사 요약을 구현
- **image :** 이미지 생성을 구현
- **keyword :** 키워드 추출 구현
- **connect_server :** 스프링 서버와 통신을 위한 API구현
