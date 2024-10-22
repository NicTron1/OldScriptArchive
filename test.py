from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import names
import string 
import random 
import requests
from selenium.webdriver.support.ui import Select
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from webdriver_manager.chrome import ChromeDriverManager
import pickle


def atcTask(link): 
    driver = webdriver.Firefox(executable_path="C:\\Users\\compu\\Documents\\Programs and Scripts\\geckodriver.exe")
    driver.get(link)
    driver.implicitly_wait(9999999999)
    driver.find_element_by_class_name('add-to-cart-button').click()
    time.sleep(5)
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    driver.quit()
    time.sleep(2)
    return "Carted"
    


print(atcTask("https://www.bestbuy.com/site/dynex-3-usb-type-a-to-lightning-charge-and-sync-cable-white/6403442.p?irclickid=yOIxA5zO2xyLT2y05-R4sULoUkE1rl093y8BXg0&irgwc=1&ref=198&loc=YieldKit%20GmbH&acampID=0&mpid=357605&skuId=6403442"))


driver = webdriver.Firefox(executable_path="C:\\Users\\compu\\Documents\\Programs and Scripts\\geckodriver.exe")
cookies = pickle.load(open("cookies.pkl", "rb"))
driver.get('https://www.bestbuy.com')
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(1)
driver.get('https://www.bestbuy.com/cart')


