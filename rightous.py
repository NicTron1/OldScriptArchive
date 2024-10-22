from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import names
import string 
import random 
from selenium.webdriver.support.ui import Select
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
count = 0
amount = 10

while count < amount:
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-data-dir=C:\\Users\\compu\\AppData\\Local\\Google\\Chrome\\User Data")

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(5)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc1j3ebEcEQvGZUSnx0qT6Wv6QbIcbPKrRg08gAQ3eTk0NO6Q/viewform')
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('LOL GOSSIP')
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('LOL')
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('@foxnews')
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Great Form')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').submit()
    
    time.sleep(2)
    driver.quit()