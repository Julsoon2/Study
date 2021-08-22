from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 900)") # 화면 해상도에 따라서 1600*900 이라서 900만큼 내리기 실행. 0이 최상단

# 현재 화면의 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 3

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 다시 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml") # selenium 객체로부터 html 소스 받아옴

# movies = soup.find_all("div", attrs = {"class":["ImZGtf mpg5gc", "WsMG1c nnK0zc"]}) # 리스트로 전달하면 리스트에 해당하는 애들 다 가져옴
movies = soup.find_all("c-wiz", attrs = {"jsrenderer":"PAQZbb"}) # 위에거 하니까 두개씩 찾아져서 그냥 이걸루
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격
    original_price = movie.find("span", {"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "  <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", {"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    # 링크 정보
    if movie.find("a", attrs ={"class":"mnKHRc"})["href"]:
        link = movie.find("a", attrs ={"class":"mnKHRc"})["href"]
    else:
        continue
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()