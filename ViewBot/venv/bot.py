import selenium
import time

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

def viewTask(link):
    try:
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
        raw_user = user_agent_rotator.get_random_user_agent()
        user = "user-agent={}".format(raw_user)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(user)

        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.implicitly_wait(10)

        driver.get(link)
        driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button').click()
        time.sleep(3)
        driver.quit()
        print('View Given')
    except:
        print('Error')

count = 0
amount = 263

while count < amount:
    viewTask('https://www.youtube.com/watch?v=vy5OIRcCFZs&ab_channel=AlexN')
    count += 1

