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

devocean = "https://devocean.sk.com/blog/sub/index.do?ID=&boardType=&searchData=&page={}&subIndex=%EC%B5%9C%EC%8B%A0+%EA%B8%B0%EC%88%A0+%EB%B8%94%EB%A1%9C%EA%B7%B8"

devo_title = []
devo_link = []
devo_date = []

# title, date, link
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(1, 62):
    driver.get(devocean.format(i))

    page = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/section[2]/div/div[2]/div/ul')
    for j in range(1, 11):
        driver.implicitly_wait(5)
        title = page.find_element(By.CSS_SELECTOR, "#wrapper > div > section.sub-sec.blog.cont01 > div > div.sub-sec-aside > div > ul > li:nth-child({}) > div > a > h3".format(j))
        devo_title.append(title.get_attribute("textContent").strip())

        link = page.find_element(By.CSS_SELECTOR, "#wrapper > div > section.sub-sec.blog.cont01 > div > div.sub-sec-aside > div > ul > li:nth-child({}) > div > a".format(j))
        devo_link.append(link.get_attribute("href").strip())

        date = page.find_element(By.CSS_SELECTOR, "#wrapper > div > section.sub-sec.blog.cont01 > div > div.sub-sec-aside > div > ul > li:nth-child({}) > div > div.sec-box > div > div.author-area.pc_view > span.date".format(j))
        devo_date.append(date.get_attribute("textContent").strip())

# tags
devo_tag_list = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(1, 62):
    driver.get(devocean.format(i))

    for j in range(1, 11):
        devo_tag = []
        title = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/section[2]/div/div[2]/div/ul/li[{}]/div/div[1]/div/div[1]'.format(j))
        tags = title.find_elements(By.TAG_NAME, "span")

        for tag in tags:
            devo_tag.append(tag.get_attribute("textContent").replace("#", ""))
        devo_tag_list.append(list(devo_tag))

    time.sleep(1)

# to_csv
devocean_df = pd.DataFrame({'title':devo_title, 'date':devo_date, 'tags':devo_tag_list, 'company':'데보션', 'link':devo_link})
devocean_df.to_csv("devocean.csv", index=False)