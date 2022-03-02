from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.baidu.com')
try:
    driver.find_element(By.ID, 'kkw')
    print('pass: is found')
except Exception as e:
    print('fail: not found\n{}'.format(e))
driver.quit()
