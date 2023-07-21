# 매개변수: search_word, save_name(==title)
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request
import os



def gen_image(id, search_word):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://pollinations.ai/")


    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/input').send_keys(search_word)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/button').click()

    driver.switch_to.window(driver.window_handles[-1])


    url = driver.current_url
    save_name = f"C:\images\{id}.png"
    urllib.request.urlretrieve(url, save_name)

    
    #os.remove(save_name)
    driver.quit()
    result={
        'id':id,
        'path':save_name
    }
    return result
    
