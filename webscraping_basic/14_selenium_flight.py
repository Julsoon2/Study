from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window() # 창 최대화

url = "https://beta-flight.naver.com/"
browser.get(url) # url로 이동

# 가는 날 xpath를 찾아 클릭
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 가는날 오는날 xpath로 클릭 * 시간대기 없으면 에러나니 적당히 지연시간 주기
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/button/b')))
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/button/b').click()
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/button/b')))
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/button/b').click()

# 도착지 클릭
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[3]/i[1]').click()

# 검색 클릭
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 특정 시간동안 기다리고, 그동안 반응왔다면 바로 진행. 보통 예외처리랑 같이 진행 : 근데 계속 에러나서 그냥 진행..
# try:
elem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/b/i')))
# finally:
    # browser.quit() # 실패하면 바로 브라우저 종료

# 첫번째 결과 출력
elem = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/b/i')
print(elem.text + "원")