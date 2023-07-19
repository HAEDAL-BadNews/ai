# 매개변수: search_word, save_name(==title)
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pollinations.ai/")

search_word = '파이썬, 사냥'

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/input').send_keys(search_word)
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/button').click()

driver.switch_to.window(driver.window_handles[-1])

# img 생성 함수 호출시 매개변수로 savename(==title) 받아올것
url = driver.current_url
save_name = "test.png"
urllib.request.urlretrieve(url, save_name)

#if not os.path.isdir(img_folder_path):
#   os.mkdir(img_folder_path)

driver.quit()
