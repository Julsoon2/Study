from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome("./chromedriver.exe", options=options)

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# # 3. 아이디와 비번 입력

# 기존 입력값 지우기
# browser.find_element_by_id("id").clear()

# browser.find_element_by_id("id").send_keys("freefruit")
# browser.find_element_by_id("pw").send_keys("ghfk2wms-1")
# send_keys 방식으로는 캡챠에 걸려버림

# 3.2. captcha 우회해서 로그인 js로 입력하는 방식
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "freefruit", pw = "ghfk2wms-1")

time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
# 기존 입력값 지우기
browser.find_element_by_id("id").clear()
browser.execute_script(input_js)

# 4. 로그인 버튼 클릭
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
elem = browser.find_element_by_id("log.login").click()

# 5. html 정보 출력
print(browser.page_source)

# 6. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저  료