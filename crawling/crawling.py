import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

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

news_title = soup.select_one('div.sh_text>a')
print(news_title.text)
