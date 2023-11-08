# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pickle

# header
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
# 데이터 리스트
data = []
# 회사 이름
company_name = "뱅크샐러드"
for i in range(1, 4):
    # 페이지 별 url 요청
    page_res = requests.get(f"https://blog.banksalad.com/tech/page/{i}/",  user_agent)
    page_html = page_res.content.decode('utf-8', 'replace') 
    page_soup = BeautifulSoup(page_html, "html.parser")
    
    for post in page_soup.find_all("div", "post_card"):    
        # 각 post별 url    
        url = "https://blog.banksalad.com" + post.find("h2","post_title").find("a")["href"]
        
        # post별 url 요청
        res = requests.get(url,  user_agent)
        html = res.content.decode('utf-8', 'replace') # 글자가 깨져서 적용
        soup = BeautifulSoup(html, "html.parser")
        
        # 제목, 날짜, 태그들 수집 
        pub_date = soup.find("div","post_details").find("span").text
        title = soup.find("h1").text
        tags = []
        for tag in soup.find("div","post_tags").find_all("a"):
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

# 수집된 데이터 파일 저장       
with open("../data/banksalad.pkl", "wb") as f:
    pickle.dump(data, f)