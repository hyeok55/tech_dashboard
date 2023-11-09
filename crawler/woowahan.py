# 필요한 라이브러리 불러오기
from time import sleep
import pickle

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# header            
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}    
# 데이터 리스트
data = []
# 회사 이름
company_name = "우아한형제들"

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    # 브라우저 창 최대화
    driver.maximize_window()
    driver.get("https://techblog.woowahan.com/")
    # post의 url 리스트 
    urls = []
    while True:
        sleep(1)
        for post in driver.find_element(By.CLASS_NAME, "posts").find_elements(By.CLASS_NAME, "item")[10:]:
            # post의 url 수집
            urls.append(post.find_element(By.TAG_NAME, "a").get_attribute("href"))
        # 스크롤을 최대로 내림
        prev_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(2)
            curr_height = driver.execute_script("return document.body.scrollHeight")
            if curr_height == prev_height:
                break
            prev_height = curr_height
        # 다음 페이지 버튼 클릭
        button = driver.find_elements(By.CLASS_NAME, "nextpostslink")
        if button:
            ActionChains(driver).click(button[0]).perform()
        else:
            break
        
for url in urls:
    # post별 url 요청
    res = requests.get(url, user_agent)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # 제목, 날짜, 태그들 수집 
    title = soup.find("h1").text
    pub_date = soup.find("div", "author").find("span").text.strip()
    tags = []
    for tag in soup.find("span","cats").find_all("a", "cat-tag"):
        tags.append(tag.text.strip())
        
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
with open("../data/woowahan.pkl", "wb") as f:
    pickle.dump(data, f)