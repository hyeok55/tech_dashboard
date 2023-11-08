# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pickle

# header
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
# 데이터 리스트
data = []
# 회사 이름
company_name = "하이퍼커넥트"

# 게시글 리스트 페이지 url 요청
res = requests.get("https://hyperconnect.github.io/", user_agent)
soup = BeautifulSoup(res.text, "html.parser")
for post in soup.find("ul","post-list").find_all("li"):
    # 각 post별 url, 제목, 날짜, 태그들 수집
    url = "https://hyperconnect.github.io" + post.find("a")["href"]
    title = post.find("a").text.strip()
    pub_date = post.find("time").text
    tags = []
    for tag in post.find("span", "tags").find_all("a"):
        tags.append(tag.find("span").text)
    
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
with open("../data/hyperconnect.pkl", "wb") as f:
    pickle.dump(data, f)