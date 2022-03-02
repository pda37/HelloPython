from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox()  # 打开火狐浏览器
driver = webdriver.Chrome()  # 打开谷歌浏览器
driver.maximize_window()   # 最大化浏览器窗口
'''
implicitly_wait():隐式等待
当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
'''
driver.implicitly_wait(5)  # 设置隐式时间等待
driver.get('https://test.gelonghui.com/')  # 访问地址
# 定位到输入框并输入关键字“新之助”
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/header/section[2]/section/div[2]/input').send_keys('新之助')
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/header/section[2]/section/div[2]/span').click()  # 点击搜索按钮
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/section/div/div[1]/div[2]/ul/li[5]').click()
time.sleep(3)  # 等待3s
# 使用is_displayed()方法判断元素是否在页面显示
r = driver.find_element(By.XPATH, '//*[@id="search-user"]/div/section/a/span[text()="春日部炸子鸡"]').is_displayed()
print(r)
driver.quit()  # 关闭浏览器
