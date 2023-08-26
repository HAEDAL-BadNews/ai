import requests
from bs4 import BeautifulSoup as bs
from random import sample
import sys
import os
# import keyword_naitive
import crawling.keyword_naitive as keyword_naitive

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from huggingface import summarize_context
# from summarize.huggingface import summarize_context


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


def get_articles(category: str, userId: str):
    base_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1="

    category_code = category_dict[category]
    response = requests.get(f"{base_url}{category_code}", headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_titles = soup.select('a.sh_text_headline')
    news_authors = soup.select('div.sh_text_press')
    #news_images = soup.select('div.sh_thumb_inner')

    news = []

    article_num = min(5, len(news_titles))

    # 카테고리 페이지에서 얻을 수 있는 기본 정보
    for i in range(article_num):
        news_object = {
            'title': news_titles[i].text,
            'url': news_titles[i].attrs['href'],
            'author': news_authors[i].text,
            'category': category,
            'userId': userId,
            #'image': {"id":0,
                  #"path":news_images[i].find('img').attrs['src']}
        }
        news.append(news_object)

    # 각 기사 페이지 접근
    for i in range(article_num):
        base_url = news[i]['url']
        response = requests.get(base_url, headers=headers)
        html_text = response.text
        soup = bs(html_text, 'html.parser')

        # date
        news_date = soup.select_one('span._ARTICLE_DATE_TIME').attrs['data-date-time']
        news[i]['date'] = news_date

        # image
        news_image = soup.find(id='img1');
        if news_image:
            news_image = news_image.get('data-src')
        else:   # no image
            news_image = soup.select_one('#contents > div._VOD_PLAYER_WRAP')
            if news_image:
                news_image = news_image.attrs['data-cover-image-url']
            else:   # no video too
                i -= 1
        news[i]['image'] = {"id":0,
                            "path":news_image}

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

        # 요약
        news[i]['context'] = news_content[:150]
        # 이래도 600 ~ 1700자 정도 나옴

        # 키워드 제목에서 추출하기
        keyTitle = news_titles[i].text.replace('\n', ' ').replace('\\', ' ').replace('.', ' ') \
            .replace(',', ' ').replace('\'', ' ')
        keyTitle = list(map(str, keyTitle.split()))

        keyword_idx = sample(range(len(keyTitle)), min(5, len(keyTitle)))
        keywords = []
        for j in keyword_idx:
            keywords.append(keyTitle[j])
        news[i]['keywords'] = keywords

    return (news)


def get_one_article(category: str, userId: str):
    base_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1="

    category_code = category_dict[category]
    response = requests.get(f"{base_url}{category_code}", headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_titles = soup.select('a.sh_text_headline')
    news_authors = soup.select('div.sh_text_press')
    #news_images = soup.select('div.sh_thumb_inner')

    news_object = {
        'title': news_titles[0].text,
        'url': news_titles[0].attrs['href'],
        'author': news_authors[0].text,
        'category': category,
        'userId': userId,
        #'image': {"id":0,
        #          "path":news_images[0].find('img').attrs['src']}
    }
    news = news_object

    # 각 기사 페이지 접근
    base_url = news['url']
    response = requests.get(base_url, headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_date = soup.select_one(
        'span._ARTICLE_DATE_TIME').attrs['data-date-time']

    news['date'] = news_date

    # image
    while True:
        news_image = soup.find(id='img1');
        if news_image:
            news_image = news_image.get('data-src')
            break
        else:  # no image
            news_image = soup.select_one('#contents > div._VOD_PLAYER_WRAP')
            if news_image:
                news_image = news_image.attrs['data-cover-image-url']
                break
            else:  # no video too
                continue
    news['image'] = {"id": 0,
                     "path": news_image}


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
    news['context'] = news_content[:150]

    # 키워드 제목에서 추출하기
    keyTitle = news_titles[0].text.replace('\n', ' ').replace('\\', ' ').replace('.', ' ')
    keyTitle = list(map(str, keyTitle.split()))
 
    idx = sample(range(len(keyTitle)), min(5, len(keyTitle)))
    keywords = []
    for i in idx:
        keywords.append(keyTitle[i])
    news['keywords'] = keywords


    return news


def get_home_articles(category: str, userId: str):
    base_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1="
    categories = sample(list(category_dict), 5)

    news = []
    for category in categories:
        news.append(get_one_article(category, userId))

    return (news)