# 필요한 라이브러리 불러오기
import pickle
from time import sleep
import requests
from bs4 import BeautifulSoup

# header
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
# 데이터 리스트
data = []
# 회사 이름
company_name = "무신사"

# 테크 블로그 홈 url 요청
base_res = requests.get("https://medium.com/musinsa-tech", user_agent)
base_soup = BeautifulSoup(base_res.text, "html.parser")

for menu in base_soup.find("div", "collectionHeader-blockNav").find_all("li")[:5]:
    # 메뉴 별 url 요청
    menu_url = menu.find("a")["href"]
    page_res = requests.get(menu_url, user_agent)
    page_soup = BeautifulSoup(page_res.text, "html.parser")
    
    for post in page_soup.find_all("div","postArticle"):
        # 각 post별 url
        url = post.find_all("a")[3]["href"]
        # post별 url 요청
        res = requests.get(url, user_agent)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 제목, 날짜, 태그들 수집 
        title = soup.find("h1").text
        pub_date = soup.find("span", attrs={"data-testid": "storyPublishDate"}).text
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
with open("../data/musinsa.pkl", "wb") as f:
    pickle.dump(data, f)