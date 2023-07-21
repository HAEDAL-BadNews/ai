import requests
from bs4 import BeautifulSoup as bs
import sys, os
import crawling.keyword_naitive as keyword_naitive
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from summarize.huggingface import summarize_context

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

category_dict = {
    '정치':'100',
    '경제':'101',
    '사회':'102',
    '생활/문화':'103',
    '세계':'104',
    'IT/과학':'105'
}

def get_articles(category: str):
    base_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1="

    category_code = category_dict[category]
    response = requests.get(f"{base_url}{category_code}", headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news = []
    len = 5
    news_titles = soup.select('a.sh_text_headline')
    news_authors = soup.select('div.sh_text_press')
    for i in range(len):
        news_object = {
            'title': news_titles[i].text,
            'url': news_titles[i].attrs['href'],
            'author': news_authors[i].text,
            'category': category,
        }
        news.append(news_object)


    print("페이지 기사 얻어오기")
    # 각 기사 페이지 접근
    driver = keyword_naitive.init_keyword_naitive()
    
    for i in range(len):
        base_url = news[i]['url']
        response = requests.get(base_url, headers=headers)
        html_text = response.text
        soup = bs(html_text, 'html.parser')

        news_date = soup.select_one(
            'span._ARTICLE_DATE_TIME').attrs['data-date-time']
        
        news[i]['date'] = news_date[0:10]

        news_content = soup.select_one('#dic_area').text
        print(f"요약{i}")
        news_content = summarize_context(news_content)
        news[i]['context'] = news_content


        #수정필요
        news[i]['keywords'] = ['파이썬','자바','코틀린']
        keyword_text = keyword_naitive.get_keyword_naitive(driver, news[i]['context'])
        keyword = keyword_text.split(',')
        news[i]['keywords'] = keyword[:5]

        
        return(news[i])


    # 키워드
    keyword_naitive.quit_keyword_naitive(driver)

    
    for i in range(len):
        print(news[i])
        print()
    
    return news[0]






def get_one_article(category: str, userId:str):
    base_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1="

    category_code = category_dict[category]
    response = requests.get(f"{base_url}{category_code}", headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')



    news_titles = soup.select('a.sh_text_headline')
    news_authors = soup.select('div.sh_text_press')
    
    news_object = {
        'title': news_titles[0].text,
        'url': news_titles[0].attrs['href'],
        'author': news_authors[0].text,
        'category': category,
        'userId': userId,
    }
    news = news_object


    print("페이지 기사 얻어오기")
    # 각 기사 페이지 접근
    driver = keyword_naitive.init_keyword_naitive()
    
    base_url = news['url']
    response = requests.get(base_url, headers=headers)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    news_date = soup.select_one(
        'span._ARTICLE_DATE_TIME').attrs['data-date-time']
        
    news['date'] = news_date[0:10]

    news_content = soup.select_one('#dic_area').text
    print("요약")
    news_content = summarize_context(news_content)
    news['context'] = news_content


    #수정필요
    news['keywords'] = ['파이썬','자바','코틀린']
    keyword_text = keyword_naitive.get_keyword_naitive(driver, news['context'])
    keyword = keyword_text.split(',')
    news['keywords'] = keyword[:5]

    

    # 키워드
    keyword_naitive.quit_keyword_naitive(driver)

    print(news)
    return news