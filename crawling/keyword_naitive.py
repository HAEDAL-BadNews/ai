import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json

with open('./secret.json') as f:
    secrets = json.loads(f.read())
LOGIN_ID = secrets["LOGIN_ID"]
LOGIN_PASSWORD = secrets["LOGIN_PASSWORD"]

global answer_count
answer_count = 1


def init_keyword_naitive():
    """
    백그라운드에 셀레니움 실행 (최초 1회)
    """
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # 백그라운드
    # chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.native.me/chat")

    # 로그인
    driver.implicitly_wait(60)
    driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').click()
    driver.find_element(
        By.XPATH, ' //*[@id="__next"]/div/main/div/div/div/div[1]/div[4]/div[2]/button[1]').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(60)
    driver.find_element(
        By.XPATH, '//*[@id="loginId--1"]').send_keys(LOGIN_ID)
    driver.find_element(
        By.XPATH, '//*[@id="password--2"]').send_keys(LOGIN_PASSWORD)
    driver.find_element(
        By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    driver.switch_to.window(driver.window_handles[0])

    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(
        '내가 이제 물어보는 기사의 키워드를 3~5개정도 추출해줘. 쓸데없는 말 없이 키워드만. 각 키워드는 쉼표로 구분해.\n')
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))

    return driver


def get_keyword_naitive(driver: webdriver, article: str) -> str:
    """
    이미 백그라운드에 실행중인 셀레니움 통해 naitive에게 질문, 답 듣기
    """
    global answer_count

    driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(article + '\n')

    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))
    keywords_element = driver.find_element(
        By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[2]/div[2]/div/div/div/div/div[{answer_count * 4}]/div[2]/div/div/div/p')
    answer_count += 1
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))
    keywords = keywords_element.get_attribute('innerText')
    print(keywords)
    
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(
        '내가 이제 물어보는 기사의 키워드를 3~5개정도 추출해줘. 쓸데없는 말 없이 키워드만. 각 키워드는 쉼표로 구분해.\n')
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))

    return keywords


def quit_keyword_naitive(driver: webdriver):
    """
    셀레니움 종료
    """
    driver.quit()


def whole_sequence(article: str):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # 백그라운드
    # chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.native.me/chat")

    # 로그인
    driver.implicitly_wait(60)
    driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').click()
    driver.find_element(
        By.XPATH, ' //*[@id="__next"]/div/main/div/div/div/div[1]/div[4]/div[2]/button[1]').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(60)
    driver.find_element(
        By.XPATH, '//*[@id="loginId--1"]').send_keys('rnjs5540')
    driver.find_element(
        By.XPATH, '//*[@id="password--2"]').send_keys('dydals7417!')
    driver.find_element(
        By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    driver.switch_to.window(driver.window_handles[0])

    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(
        '내가 이제 물어보는 기사의 키워드를 3~5개정도 추출해줘. 쓸데없는 말 없이 키워드만. 각 키워드는 쉼표로 구분해.\n')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))


    global answer_count

    driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(article + '\n')
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))
    
    keywords_element = driver.find_element(
        By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[2]/div[2]/div/div/div/div/div[{answer_count * 4}]/div[2]/div/div/div/p')
    answer_count += 1
    keywords = keywords_element.get_attribute('innerText')
    print(keywords)

    #driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(
#        '내가 이제 물어보는 기사의 키워드를 3~5개정도 추출해줘. 쓸데없는 말 없이 키워드만. 각 키워드는 쉼표로 구분해.\n')
    
    #WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
     #   (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))

    """
    셀레니움 종료
    """
    print('끝')
    driver.quit()

#whole_sequence('삼성전자, LG디스플레이 등 국내 대표 반도체·디스플레이 기업들이 올해 4분기를 기점으로 흑자전환에 성공할 것이라는 전망이 나온다. 지난 2분기 반도체와 디스플레이 사업에서 사상 최대 적자를 기록하며 바닥을 찍은 두 기업은 3분기부터 시황 개선에 따른 수혜가 예상된다.21일 증권가에 따르면 삼성전자의 경우 이르면 올 4분기에 반도체 사업에서 소폭 흑자가 가능할 것으로 알려졌다. 시장에서는 올 3분기부터 삼성전자의 메모리 감산 효과가 본격적으로 나타나면서 적자 폭이 크게 줄고 반등이 가능할 것이라는 분석이 나온다.주요 증권사에선 삼성전자의 올 2분기 반도체 부문 영업손실을 4조원대로 추정하고 있으며 이 중 메모리 사업부의 영업적자가 약 3조8000억원에 달했을 것으로 분석하고 있다. 올 3분기에는 영업적자 규모가 2조원대로 크게 줄어들 것이라는 설명이다. 감산 효과와 함께 D램, 낸드플래시 평균판매단가(ASP)가 안정될 것으로 관측된다.삼성전자와 SK하이닉스, 마이크론 등 D램 3강은 지난해와 올해에 걸쳐 적극적인 감산을 진행 중이다. 삼성전자의 경우 지난 4월부터 웨이퍼 투입을 줄이기 시작했다. 웨이퍼 투입에서 생산까지 걸리는 주기가 3~6개월 정도이기 때문에 올 3분기부터 감산 효과가 나오기 시작한다. 대만 시장조사업체 트렌드포스는 올해 2분기 D램 가격 하락 폭은 전 분기 대비 13~18%일 것으로 추정됐으나 3분기에는 가격 하락세가 0~5%로 완화될 것으로 전망했다.김동원 KB증권 연구원은 “3분기부터 D램 평균판매단가(ASP)가 고부가 신제품(HBM3, DDR5) 출하 증가와 감산에 따른 공급 축소 효과로 2021년 3분기 이후 7개 분기 만에 상승 전환할 것으로 전망된다”면서 “수요에 대한 가격 탄력성이 높은 낸드플래시 평균판매단가의 경우 하락 지속이 불가피하지만 가격 하락 둔화로 적자 축소가 예상된다”고 설명했다.')