import pyautogui
from pyautogui import moveTo
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By


import os
import urllib3
import getpass
path_input = getpass.getuser()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
chromedriver_autoinstaller.install(True)


#옵션 - 셀레니움
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink_features=AutomationControlled")
options.add_experimental_option("excludeSwitches",["enable_logging"])
options.add_argument("no_sandbox")
options.add_argument("--start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extionsions")
options.add_experimental_option("useAutomationExtension",False)
#options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)



# 다음 검색

# Open a new Chrome window and navigate to Daum website
driver = webdriver.Chrome()
driver.get('https://www.daum.net/')

# Find the search box and type '네이버 쇼핑'
daum_search_box = driver.find_element(By.NAME,'q')
daum_search_box.send_keys('네이버쇼핑')

# Press the Enter key
daum_search_box.send_keys(Keys.ENTER)


# Wait for the search results to load
time.sleep(3)


# '네이버 쇼핑' 검색
naver_search_button = driver.find_element(By.CLASS_NAME,'f_tit')
naver_search_button.click()
time.sleep(3)

# get the current URL of the page
current_url = driver.current_url

# set the keyword you want to search for
keyword = "침대"

# move the mouse to the address bar and click to focus
pyautogui.moveTo(226, 157)
time.sleep(2)
pyautogui.click()
time.sleep(5)

# copy the keyword to the clipboard
pyperclip.copy(keyword)
time.sleep(3)

# simulate pressing Ctrl+V to paste the keyword into the address bar
pyautogui.keyDown('ctrl')
time.sleep(3)
pyautogui.press('v')
time.sleep(3)
pyautogui.keyUp('ctrl')


# simulate pressing Enter to initiate the search
pyautogui.press('enter')
print('done')
# wait for the search results to load
time.sleep(1000)









# Close the browser window
driver.quit()





# move the mouse to the top search result and click to select it
# pyautogui.moveTo(500, 500)
# pyautogui.click()



