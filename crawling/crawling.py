import requests
from bs4 import BeautifulSoup as bs
from random import sample
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

category_dict = {
    '정치': '100',
    '경제': '101',
    '사회': '102',
    '생활/문화': '103',
    '세계': '104',
    'IT/과학': '105'
}


def get_some_articles(category: str, userId: str, num_to_get: int):
    base_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1="

    category_code = category_dict[category]
    response = requests.get(f"{base_url}{category_code}", headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_titles = soup.select('a.sh_text_headline')
    news_authors = soup.select('div.sh_text_press')
    news = []

    # num_to_get = 5

    # 카테고리 페이지에서 얻을 수 있는 기본 정보
    for i in range(num_to_get):
        news_object = {
            'title': news_titles[i].text,
            'url': news_titles[i].attrs['href'],
            'author': news_authors[i].text,
            'category': category,
            'userId': userId,
        }

        # 키워드 제목에서 추출하기
        keyTitle = news_titles[i].text.replace('\n', ' ').replace('\\', ' ').replace('.', ' ').replace(',', ' ').replace(
            '\'', ' ')
        keyTitle = list(map(str, keyTitle.split()))
        idx = sample(range(len(keyTitle)), 5)
        keywords = [keyTitle[i] for i in idx]
        news_object['keywords'] = keywords

        # 기사 본문
        get_article_content(news_object['url'], news_object)

        news.append(news_object)

    return news


def get_home_articles(category: str, userId: str):
    categories = sample(list(category_dict), 5)
    news = []
    for category in categories:
        news.append(get_some_articles(category, userId, 1)[0])

    return news


def get_article_content(url: str, news_object: dict):
    # 기사 페이지 접근
    response = requests.get(url, headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_date = soup.select_one(
        'span._ARTICLE_DATE_TIME').attrs['data-date-time']
    news_object['date'] = news_date[0:10]

    # 본문 - 기사 위쪽 굵은글씨 문단 추출 및 제거
    naver_summary_selecors = ['#dic_area > b', '#dic_area > strong', '#dic_area > div']
    for selector in naver_summary_selecors:
        naver_summary = soup.select_one(selector)
        if naver_summary:
            naver_summary.extract()
            break
    strong_tags = soup.find_all('strong')
    for strong_tag in strong_tags:
        strong_tag.extract()

    # 본문 - 이미지 설명 추출 및 제거
    image_desc_selecors = ['#dic_area > span > em', '#dic_area > div > div > span.end_photo_org > em',
                           '#dic_area > div:nth-child(1) > figure > figcaption']
    for selector in image_desc_selecors:
        image_desc = soup.select_one(selector)
        if image_desc:
            image_desc.extract()
            break
    img_desc_elements = soup.select('.img_desc')
    for img_desc_element in img_desc_elements:
        img_desc_element.extract()
    img_desc_elements = soup.find_all('nbd_table')
    for img_desc_element in img_desc_elements:
        img_desc_element.extract()

    # 본문 - 개행문자 제거 추가
    news_content = soup.select_one('#dic_area').text.strip().replace('\n', '').replace('\\', '')

    # 요약: pytorch model 서버 램 부족으로 삭제
    # news_content = summarize_context(news_content)
    news_object['context'] = news_content[:150]
