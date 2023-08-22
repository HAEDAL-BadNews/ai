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

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # 백그라운드
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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # 백그라운드
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

    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/textarea').send_keys(
        '내가 이제 물어보는 기사의 키워드를 3~5개정도 추출해줘. 쓸데없는 말 없이 키워드만. 각 키워드는 쉼표로 구분해.\n')
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div/div/form/div/button')))

    """
    셀레니움 종료
    """
    print('끝')
    driver.quit()

