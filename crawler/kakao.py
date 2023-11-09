import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

user_agent = user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

kakao = "https://tech.kakao.com/blog/"

kakao_title = []
kakao_link = []
kakao_date = []

# title, date, link
for i in range(1, 36):
    res = requests.get(kakao+"page/{}/#posts".format(i), user_agent)
    soup = BeautifulSoup(res.text, "html.parser")
    soup.find("section", class_="elementor-section elementor-top-section elementor-element elementor-element-2252c9ab elementor-section-boxed elementor-section-height-default elementor-section-height-default").decompose()

    ktitle = soup.find_all("article", "elementor-post")
    for title in ktitle:
        kakao_title.append(title.find("div", "elementor-post__text").find("h3", "elementor-post__title").a.text.strip())
        kakao_link.append(title.find("div", "elementor-post__text").find("h3", "elementor-post__title").a["href"])
        kakao_date.append(title.find("div", "elementor-post__text").find("div", "elementor-post__meta-data").find("span", "elementor-post-date").text.strip())
    time.sleep(1)

# tags
kakao_tag_list = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for link in kakao_link:
    kakao_tag = []
    driver.get(link)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    tags = soup.find_all("a", "elementor-post-info__terms-list-item")
    for tag in tags:
        kakao_tag.append(tag.text)
    kakao_tag_list.append(list(kakao_tag))

# to_csv
kakao_df = pd.DataFrame({'title':kakao_title, 'date':kakao_date, 'tags':kakao_tag_list, 'company':'카카오', 'link':kakao_link})
kakao_df.to_csv("kakao.csv", index=False)