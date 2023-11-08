from time import sleep
import pickle

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# header            
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}    
# 데이터 리스트
data = []
# 회사 이름
company_name = "왓챠"

# 테크 블로그 홈 url 요청
base_res = requests.get("https://medium.com/watcha/", user_agent)
base_soup = BeautifulSoup(base_res.text, "html.parser")

for menu in base_soup.find_all("li", "collectionHeader-navItem")[:6]:
    # 메뉴 별 url
    menu_url = menu.find("a")["href"]
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        # 브라우저 창 최대화
        driver.maximize_window()
        driver.get(menu_url)
        sleep(1)
        # 스크롤을 최대로 내림
        prev_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(2)
            curr_height = driver.execute_script("return document.body.scrollHeight")
            if curr_height == prev_height:
                break
            prev_height = curr_height
            
        for post in driver.find_elements(By.CLASS_NAME, "streamItem.streamItem--postPreview.js-streamItem"):
            # 각 post별 url
            url = post.find_elements(By.TAG_NAME, "a")[3].get_attribute("href")
            # post별 url 요청
            res = requests.get(url, user_agent)
            soup = BeautifulSoup(res.text, "html.parser")
            
            # 제목, 날짜, 태그들 수집 
            title = soup.find("title").text.split(". ")[0]
            pub_date = soup.find("span", attrs={"data-testid" : "storyPublishDate"}).text
            tags = []
            for candidates in soup.find_all("a", rel="noopener follow"):
                if candidates["href"].startswith("/tag"):
                    tags.append(candidates.text)
                
            # 최종 데이터 dictionary 및 데이터 리스트에 추가
            elem = {
                    "title" : title,
                    "company_name" : company_name,
                    "pub_date" : pub_date,
                    "url" : url,
                    "tags" : tags
                }
            data.append(elem)
            # 요청 간 텀을 주기 위함
            sleep(0.5)
        
# 수집된 데이터 파일 저장 
with open("../data/watcha.pkl", "wb") as f:
    pickle.dump(data, f)