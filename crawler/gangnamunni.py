# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

from time import sleep
import pickle

# header
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
# 데이터 리스트
data = []
# 회사 이름
company_name = "강남언니"

# 페이지 별 url 요청
page_res = requests.get("https://blog.gangnamunni.com/blog/tech/", user_agent)
page_html = page_res.content.decode("utf-8", "replace") # 글자가 깨져서 적용
page_soup = BeautifulSoup(page_html, "html.parser")
for post in page_soup.find("ul","post-list").find_all("li"):
    # 각 post별 url 수집
    title_url = post.find("div","post-title").find("a")
    url = "https://blog.gangnamunni.com" + title_url["href"]
    # 제목
    title = title_url.text.strip()
    
    # post별 url 요청
    res = requests.get(url, user_agent)
    html = res.content.decode("utf-8", "replace") 
    soup = BeautifulSoup(html, "html.parser")
    # 날짜, 태그들 수집
    pub_date = soup.find("div", "post-date").text.strip()
    tags = []
    for tag in soup.find("div", "post-tag-wrap").find_all("span"):
        tags.append(tag.text)
        
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
with open("../data/gangnamunni.pkl", "wb") as f:
    pickle.dump(data, f)