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
import threading
import pyautogui

proxy_data = open(r"proxies.txt","r")
lineList = proxy_data.readlines()
proxy_data.close()

threads = 1


def travTask():
    count = 0
    entries = 100
    while count < entries:
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
        raw_user = user_agent_rotator.get_random_user_agent()

        user = "user-agent={}".format(raw_user)
        rawPROXY = lineList[int(random.randrange(1, 100))].strip()
        sepPROXY = rawPROXY.split(':')
        user = sepPROXY[2]
        password = sepPROXY[3]
        PROXY = sepPROXY[0] + ":" +sepPROXY[1]
        
        print(PROXY)
        print(user)
        print(password)

        chrome_options = Options()
        chrome_options.add_argument(user)

        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        name = names.get_full_name()
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        N = 10
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N)) 
        catch = '@ntron.xyz'
        email = res + catch
        random_number = random.randint(1000000, 9999999)

        result_str = ''.join(random.choices(string.ascii_lowercase, k = 5)) 
        address = str(result_str) +" 12105 Shadow Run Blvd"


        driver.get('https://shop.travisscott.com')
        driver.implicitly_wait(30)
        time.sleep(1)
        pyautogui.typewrite(user)
        pyautogui.press('tab')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        

        try:
            driver.find_element_by_xpath('//*[@id="EMAIL-4728593645695"]').send_keys(email)
            driver.find_element_by_xpath('//*[@id="FNAME-4728593645695"]').send_keys(first_name)
            driver.find_element_by_xpath('//*[@id="LNAME-4728593645695"]').send_keys(last_name)
            driver.find_element_by_xpath('//*[@id="ZIPCODE-4728593645695"]').send_keys(33569)
            driver.find_element_by_xpath('//*[@id="TELEPHONE-4728593645695"]').send_keys("813"+str(random_number))

        except:
            print('Task Error')
        driver.quit()
        count += 1

for i in range(threads):
    task = threading.Thread(target=travTask)
    task.start()

print(threads)