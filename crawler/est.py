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
company_name = "이스트소프트"

# 이스트소프트 테크블로그 url
base_url = "https://blog.est.ai/"
for page_url in ([base_url] + [base_url + f"page{i}" for i in range(2, 5)]):
    # 페이지 별 url 요청
    page_res = requests.get(page_url, user_agent)
    page_soup = BeautifulSoup(page_res.text, "html.parser")
    
    for post in page_soup.find_all("li", "post-preview"):
        # 각 post별 url
        url = post.find("article").find("a")["href"]
        # post별 url 요청
        res = requests.get(url, user_agent)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 제목, 날짜, 태그들 수집 
        title = soup.find("h1").text
        pub_date = soup.find("span", "post-meta").text

        tags = []
        for tag in soup.find("div","blog-tags").find_all("li"):
            tags.append(tag.find("a").text)
            
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
with open("../data/est.pkl", "wb") as f:
    pickle.dump(data, f)