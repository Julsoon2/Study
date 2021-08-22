import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs = {"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"] # 속성에 해당하는 값을 가져오려면 대괄호로 쓰면 됨
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
cartoons = soup.find_all("div", attrs = {"class":"rating_type"})
total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate) # get_text로 긁어온 애는 string이기 때문에 float으로 변환해줌
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))