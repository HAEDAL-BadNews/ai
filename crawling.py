import requests
from bs4 import BeautifulSoup as bs

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

response = requests.get(url, headers=headers)
html_text = response.text
soup = bs(html_text, 'html.parser')

news = []
len = 5

news_titles = soup.select('div.sh_text>a')
for i in range(len):
    news_object = {
        'title': news_titles[i].text,
        'href': news_titles[i].attrs['href']
    }
    news.append(news_object)

news_authors = soup.select('div.sh_text_press')
for i in range(len):
    news[i]['author'] = news_authors[i].text

# 각 기사 페이지 접근
for i in range(len):
    url = news[i]['href']
    response = requests.get(url, headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_date = soup.select_one(
        'div.media_end_head_info_datestamp_bunch>span').attrs['data-date-time']
    news[i]['date'] = news_date

    news_content = soup.select_one('#dic_area').text
    news[i]['content'] = news_content
    # text 긁어와도 요약에 문제없음
