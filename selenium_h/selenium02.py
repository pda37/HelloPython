from selenium import webdriver
from selenium.webdriver.common.by import By
import re

'''
获取网页上的所有邮箱
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://home.baidu.com/home/index/contact_us')
# 方法1：获取body元素内的文本信息
doc = driver.find_element(By.TAG_NAME, 'body').get_attribute('textContent')
# 方法2：获取所有页面源代码
# doc = driver.page_source
# 使用正则，提取 xxx@xxx.xxx 的字段，保存到emails列表
emails = re.findall(r'[\w]+@[\w.-]+', doc)
# 遍历列表
for email in emails:
    print(email)
# print(doc)
driver.quit()
