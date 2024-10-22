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
import pickle



def zoomTask():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    raw_user = user_agent_rotator.get_random_user_agent()
    user = "user-agent={}".format(raw_user)
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument(user)

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    name = names.get_full_name()
    first_name = names.get_first_name()
    last_name = names.get_last_name()

    
    driver.implicitly_wait(10)
    
    
    start = False

    if start:
        driver.get('https://zoom.us/j/97696468754?pwd=eCtoL1ZxcWFnQXhYR1BMOC95eGYwUT09')
        input('Press any key to continue ')
        url = driver.current_url
        print(url)
        pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
        driver.quit()
    else: 
        link = 'https://zoom.us/wc/97696468754/join?track_id=&jmf_code=&meeting_result=&tk=&cap=03AGdBq24m5i8RgUSs10O0-QPa2d8jOrsZlbJLR4sc-TWYUsKCqu2NJ063hnvSYY9-L5vFTLe2zTFUVpOpCBNxXRsfW6703TRWvqgBztc6sLWV_P_UnwkTj-kNrP7ixBPyPMiHEoxsFG2ZD2R62IszWCPWQKe1R_sfYT0XSOP15qh-DAUq5oRCUIuB56s7oGFHnYV6NE9eh-Qm5QwXpykFOsxorAiJEPKs72Zz-9qbwX1TilZP66NEvbhwi-JcoKsE1aGjCMvMOnDDjyw0ggn8wne-W9RCfr83xPtVvcWXH0Mo3IFPQ1EBw153LHZxA5iovaoULDDpmMAYGtlunzvx-zOopEqnIlYaaZXJnCVvkm6g54ESZ53cT6kkdMGnu-2vycVjOk-IfW9q-UKT24d1eIZWcp0tUcvHku9X0rdBi_V_MMW4oqhUfJCOkWPSqhNX9W4WptijBeY7qGKIkf5f920DPayRYEv9tb0BNK15SGLWLkqJ9RMPcmchz1HcfprmXizwig_n-gkL&refTK=&wpk=wcpk88bdfe996cbe71315e060d0bf9e62b80'
        driver.get(link)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.get(link)
        time.sleep(4)
        driver.quit()

threads = 50

for i in range(threads):
    task = threading.Thread(target=zoomTask)
    task.start()
    time.sleep(1)
    