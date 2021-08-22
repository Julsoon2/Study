#%% import
import requests

#%% 1.
res = requests.get("http://google.com")

print("응답코드 :", res.status_code) #200이면 정상

#%% 2.
res = requests.get("http://1.tistory.com")

print("응답코드 :", res.status_code) #200이면 정상

#%% 3.
if res.status_code == requests.codes.ok: # 200이랑 같음
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 :", res.status_code, "]")

#%% 4.
res.raise_for_status()
print("웹 스크래핑을 진행합니다")

#%% 5.
with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)