from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True # 이거 쓰면 창 실제로 안띄우고 백그라운드에서 진행됨
options.add_argument("window-size=1600x900") # 백그라운드에서 실행될 때 창 크기 설정
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window()

# 그냥 접속하면 나오는 user-agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/92.0.4515.159 Safari/537.36

url = "https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes"
browser.get(url)

detected_value = browser.find_element_by_id("id_user_agent")
print(detected_value.text) 

# user-agent 설정 없이 실행하면 나오는 결과 :  Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# HeadlessChrome/92.0.4515.159 Safari/537.36  -> headless 크롬으로 실행하면 user-agent 값이 headlesschrome 으로 반환되는 문제 생김

browser.quit()