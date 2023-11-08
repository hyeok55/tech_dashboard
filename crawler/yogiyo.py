# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
from time import sleep
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def dynamic_web_scraping(base_url):
    """
    동적 웹페이지에 해당하는 페이지를 통한 크롤링 함수
    """
    
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        # 브라우저 창 최대화
        driver.maximize_window()
        driver.get(base_url)
        
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
            res = requests.get(url)
            soup = BeautifulSoup(res.text,"html.parser")
            
            # 제목, 날짜, 태그들 수집 
            title = soup.find("h1").text
            pub_date = soup.find("span", attrs={"data-testid" : "storyPublishDate"}).text
            tags = []
            for candidates in soup.find_all("a",rel="noopener follow"):
                if candidates["href"].startswith("https://medium.com/tag/"):
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

# header            
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}    
# 데이터 리스트
data = []

# 회사 이름
company_name = "요기요"

# https://techblog.yogiyo.co.kr/yogiyo-python/home 에서의 데이터 수집
res = requests.get("https://techblog.yogiyo.co.kr/yogiyo-python/home", user_agent)
soup = BeautifulSoup(res.text,"html.parser")
for post in soup.find_all("div", "postItem"):
    # 각 post별 url
    url = post.find("a")["href"]
    # post별 url 요청
    res = requests.get(url, user_agent)
    soup = BeautifulSoup(res.text,"html.parser")
    
    # 제목, 날짜, 태그들 수집 
    title = soup.find("h1").text
    pub_date = soup.find("span", attrs={"data-testid" : "storyPublishDate"}).text
    tags = []
    for candidates in soup.find_all("a",rel="noopener follow"):
        if candidates["href"].startswith("https://medium.com/tag/"):
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


# https://techblog.yogiyo.co.kr/tagged/post 에서의 데이터 수집
dynamic_web_scraping("https://techblog.yogiyo.co.kr/tagged/post")

# https://techblog.yogiyo.co.kr/yogiyo-tech-culture/home 에서의 데이터 수집
page_res = requests.get("https://techblog.yogiyo.co.kr/yogiyo-tech-culture/home", user_agent)
page_soup = BeautifulSoup(page_res.text, "html.parser")
for row in page_soup.find_all("div", "row u-marginTop30 u-marginLeftNegative12 u-marginRightNegative12"):
    for post in row.find_all("div", "postItem"):
        # 각 post별 url
        url = post.find("a")["href"]
        # post별 url 요청
        res = requests.get(url, user_agent)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 제목, 날짜, 태그들 수집 
        title = soup.find("h1").text
        pub_date = soup.find("span", attrs={"data-testid" : "storyPublishDate"}).text
        tags = []
        for candidates in soup.find_all("a",rel="noopener follow"):
            if candidates["href"].startswith("https://medium.com/tag/"):
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
        
        
# https://techblog.yogiyo.co.kr/tagged/interview 에서의 데이터 수집
dynamic_web_scraping("https://techblog.yogiyo.co.kr/tagged/interview")

# 수집된 데이터 파일 저장 
with open("../data/yogiyo.pkl", "wb") as f:
    pickle.dump(data, f)