import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title.get_text())
# print(soup.a) # 처음 발견되는 a 태그 불러옴
# print(soup.a.attrs) # a element의 속성 정보 반환
# print(soup.a["href"]) # a element의 href 속성의 값 출력

# print(soup.find("a", attrs = {"class":"Nbtn_upload"})) # class 가 nbtn인 a element를 찾기
# print(soup.find(attrs = {"class":"Nbtn_upload"})) # class 가 nbtn인 어떤 element를 찾기

# print(soup.find("li", attrs = {"class":"rank01"}))
# rank1 = soup.find("li", attrs = {"class":"rank01"})
# print(rank1.a.get_text())

# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text)

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text = "프리드로우-제401화 파이트 클럽 (3)")
print(webtoon)

