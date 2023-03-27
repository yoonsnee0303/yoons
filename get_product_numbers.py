import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_product_numbers(username, password, domeme_url):
    driver = webdriver.Chrome(r'C:\Users\Data2\OneDrive\바탕 화면\윤\코드\dom_to_godo\chromedriver.exe')

    # 로그인
    driver.implicitly_wait(5)
    driver.get('https://domemedb.domeggook.com/index/')

    # Click on the login button
    login_button = driver.find_element(By.XPATH,'//*[@id="rightMenu"]/li[2]/a')
    login_button.click()
    time.sleep(3)

    # Fill in the login form and submit
    username_field = driver.find_element(By.NAME, 'id')
    username_field.send_keys(username)
    time.sleep(.5)

    password_field = driver.find_element(By.NAME, 'pass')
    password_field.send_keys(password)
    login_submit_button = driver.find_element(By.CSS_SELECTOR, '#formLogin > input.formSubmit')
    login_submit_button.click()
    time.sleep(3)

    # Retrieve the product numbers from the safeDbList page
    driver.get(domeme_url)
    product_num_elements = driver.find_elements(By.CLASS_NAME, 'txt8.cur')
    product_numbers = [e.text for e in product_num_elements]

    # Close the driver
    driver.quit()

    return product_numbers