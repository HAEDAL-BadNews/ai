import requests
from bs4 import BeautifulSoup as bs
from random import sample





headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

def parsing_date(date:str):

    nalzza = date[5:15]
    nalzza = nalzza.replace(".","-")
    if date[17:19]=="오전":
        sigan = date[20:]+":00"
    else:
        si = int(date[20:22])+12
        sigan = str(si) + date[22:]+":00"

    return (nalzza +" "+ sigan)
        


def add_keyword(title:str):
    title = list(map(str, title.split()))
 
    idx = sample(range(len(title)), min(4, len(title)))
    keywords = []
    for i in idx:
        keywords.append(title[i])

    return keywords





def get_sport_articles(userId:str):
    base_url = "https://sports.news.naver.com"

    response = requests.get(f"{base_url}/index", headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')
    news_s = soup.select('li.today_item')
    result = []
    for i in range(5):
        news = news_s[i]
        news_title = news.select("strong.title")[0].text
        news_image = news.select("div.image_area")[0].find('img').attrs['src']
        news_url = base_url + news.select("a.link_today")[0].attrs['href']
        news_author = news.select("div.information > span")[0].text
        news_keyword = []
        news_keyword.append(news.select("div.information > span")[1].text)
        
        each_response = requests.get(news_url, headers=headers)
        html_text = each_response.text
        soup = bs(html_text, 'html.parser')
        
        news_date = soup.select("div.info > span")[0].text
        news_context = soup.select("#newsEndContents")[0].text
        
        


        # 전처리
        news_title = news_title.replace('\n', ' ').replace('▲', ' ').replace('\\', ' ').replace('...', ' ')
        news_context = news_context[:180].replace('\n', ' ').replace('▲', ' ').replace('\\', ' ').replace('.', ' ')
        news_keyword+=add_keyword(news_title)
        news_date = parsing_date(news_date)



        news_object = {
            "title": news_title,
            "context": news_context,
            "author": news_author,
            "url": news_url,
            "date": news_date,
            "category": "스포츠",
            "userId": userId ,
            "keyword": news_keyword,
            "image": {"id": 0,
                      "path": news_image}
        }

        result.append(news_object)



    return result

