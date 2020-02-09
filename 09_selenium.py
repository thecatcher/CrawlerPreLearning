from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import  time
from  selenium.common.exceptions  import  NoSuchElementException,TimeoutException

"""基本使用"""
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     # 找到对应的元素
#     input = browser.find_element_by_id('kw')
#     # 向该元素传递一个key
#     input.send_keys('python')
#     input.send_keys(Keys.ENTER)
#     # 设置等待时间和等待事件
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

"""选择单个元素"""
#browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# # 通过ID进行选择
# input_first = browser.find_element_by_id('q')
# # 通过CSS选择器进行选择
# input_sencond = browser.find_element_by_css_selector('#q')
# # 通过xpath进行选择
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_sencond)
# print(input_third)
# 通用方法
# input_first = browser.find_element(By.ID,'q')
# print(input_first)

"""选择多个元素"""
# browser.get('https://taobao.com')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis)
# browser.close()

"""获取对元素调用的方法"""
# browser.get('https://www.taobao.com')
#
# input = browser.find_element(By.ID,'q')
# input.send_keys('iphone')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# button = browser.find_element(By.CLASS_NAME,'btn-search')
# button.click()

"""执行JavaScript"""
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore/')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("to bottom")')

"""获取元素信息"""

# browser = webdriver.Chrome()
# url = 'http://httpbin.org/'
# browser.get(url)
# logo = browser.find_element_by_class_name('octo-body')
# print(logo.get_attribute('d'))

# 获取文本值
# browser = webdriver.Chrome()
# url = 'https://taobao.com'
# browser.get(url)
# input_demo  = browser.find_element_by_class_name('logo-bd')
# print(input_demo.text)
# browser.close()

# 获取ID,位置,标签名,大小
# browser = webdriver.Chrome()
# url = 'https://taobao.com'
# browser.get(url)
# input_demo = browser.find_element_by_class_name('logo-bd')
# print(input_demo.id)
# print(input_demo.location)
# print(input_demo.tag_name)
# print(input_demo.size)
# browser.close()

# Frame
# browser = webdriver.Chrome()
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# # 切换到父frame
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)
# browser.close()

"""等待"""
# browser = webdriver.Chrome()
# 隐式等待
# browser.implicitly_wait(10)
# browser.get('https://www.taobao.com')
# input_demo = browser.find_element_by_class_name('taobao')
# print(input_demo)
# browser.close()

# 显式等待
# browser.get('https://www.taobao.com')
# # 指定最长等待时间
# wait = WebDriverWait(browser,10)
# # 指定等待条件,如果条件成立就返回,如果条件不满足,最长等待时间超时后 返回异常
# input_demo = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input_demo,button)

"""前进后退"""

# browser = webdriver.Chrome()
#
# browser.get('https://baidu.com')
# browser.get('https://taobao.com')
# browser.get('https://cn.bing.com')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

"""cookies"""

# browser = webdriver.Chrome()
# browser.get('https://zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'brady'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

"""选项卡管理"""

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# 这个方法现在已经discarded了 新方法等我查到API再说...
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.baidu.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://cn.bing.com')


"""异常处理"""
# browser = webdriver.Chrome()
# try:
#     browser.get('http://www.baidu.com')
# except TimeoutException:
#     print('TIME OUT')
#
# try:
#     browser.find_element_by_id('hello')
#
# except NoSuchElementException:
#     print("NO ELEMENT")
# finally:
#     browser.close()




