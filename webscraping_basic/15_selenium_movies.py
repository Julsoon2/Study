import requests
from bs4 import BeautifulSoup

# header 정보가 제대로 되어있지 않으면 접속시에 default로 접속했다고 가정하고 반환 -> 미국에서 접속한걸로 간주함..
# header 정보를 제대로 입력해주자
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # 한글 페이지로 접속하게 해줌
}


url = "https://play.google.com/store/movies/top"
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs = {"class":"ImZGtf mpg5gc"})
# print(len(movies))

# with open("movie.html", "w", encoding = 'utf8') as f:
#     f.write(soup.prettify()) # res.text로 html 바로 보는것보단 soup의 prettify를 이용해 예쁘게 꾸며진걸로 보자

for movie in movies:
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text()
    print(title)