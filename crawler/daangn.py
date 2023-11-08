# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
from time import sleep
import pickle

def get_data(post_list):
    """데이터 가져오는 함수"""
    for post in post_list:
        # 각 post별 url
        url = post.find("a","link link--darken")["href"]
        # post별 url 요청
        res = requests.get(url, user_agent)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 제목, 날짜, 태그들 수집 
        title = soup.find("h1").text
        pub_date = soup.find("span",attrs={"data-testid": "storyPublishDate"}).text
        tags = []
        for candidates in soup.find_all("a",rel="noopener follow"):
            if candidates["href"].startswith("/tag"):
                tags.append(candidates.find("div").text)
                
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
company_name = "당근"

# 테크 블로그 아카이브 url 요청
base_res = requests.get("https://medium.com/daangn/archive", user_agent)
base_soup = BeautifulSoup(base_res.text, "html.parser")

for year in base_soup.find_all("div", "timebucket"):
    # 매 해 url 수집
    year_url = year.find("a")["href"]
    # 년별 url 요청
    year_res = requests.get(year_url, user_agent)
    year_soup = BeautifulSoup(year_res.text, "html.parser")
    
    months_soup = year_soup.find("div","col u-inlineBlock u-maxWidth300 u-verticalAlignTop u-lineHeight35")
    months = months_soup.find_all("div","timebucket u-inlineBlock u-width80")
    # 월별로 나눠진 경우
    if months:
        for month in months:
            # 월별 url 수집
            link_month = month.find_all("a")
            if link_month:
                month_url = link_month[0]["href"]
                # 월별 url 요청
                month_res = requests.get(month_url, user_agent)
                month_soup = BeautifulSoup(month_res.text, "html.parser")
                get_data(month_soup.find_all("div","streamItem streamItem--postPreview js-streamItem"))
    else: # 월별로 나눠지지 않은 경우
        get_data(year_soup.find_all("div","streamItem streamItem--postPreview js-streamItem"))
            
# 수집된 데이터 파일 저장              
with open("../data/daangn.pkl", "wb") as f:
    pickle.dump(data, f)