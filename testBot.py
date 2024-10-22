from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import string
import random
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-data-dir=C:\\Users\\compu\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get('https://freerice.com/categories/multiplication-table')
driver.implicitly_wait(10)
time.sleep(3)
count = int(str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[1]/div[1]/div/p[1]/strong').text).replace(",", ""))
amount = 15050

while count < amount:
    try: 
        
        
        question = str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div').text).strip()
        question1 = question.replace('x','*')
        answer = eval(question1)
        button1 = str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div').text)
        button2 = str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[3]/div').text)
        button3 = str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[4]/div').text)
        button4 = str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[5]/div').text)
    
        if button1 == str(answer):
            driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div').click()
        elif button2 == str(answer):
            driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[3]/div').click()
        elif button3 == str(answer):
            driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[4]/div').click()
        elif button4 == str(answer):
            driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[5]/div').click()
        count = int(str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[1]/div[1]/div/p[1]/strong').text).replace(",", "")) 
    except:
        
        count = int(str(driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[1]/div[1]/div/p[1]/strong').text).replace(",", ""))
    print(count)
    time.sleep(2)
    
