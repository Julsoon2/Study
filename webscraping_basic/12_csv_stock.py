import csv
import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding = 'utf-8-sig', newline = "") # newline을 넣어주지 않으면 csv row 마다  엔터가 하나씩 더쳐짐
writer = csv.writer(f) # csv 라이브러리에서 writer 객체 생성

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터 skip
            continue
        data = [column.get_text() for column in columns]
        # print(data)
        writer.writerow(data)