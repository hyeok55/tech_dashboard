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

pay = "https://tech.kakaopay.com/"

pay_title = []
pay_link = []
pay_date = []

# title, date, link
for i in range(1, 12):
    res = requests.get(pay+"page/{}".format(i), user_agent)
    soup = BeautifulSoup(res.text, "html.parser")

    ptitle = soup.find_all("li", "_postListItem_aknty_66")
    for title in ptitle:
        pay_title.append(title.find("a").find("div", "_postInfo_aknty_99").strong.text.strip())
        pay_link.append(str(pay+title.a["href"]))
        pay_date.append(title.find("a").find("div", "_postInfo_aknty_99").time.text.strip().replace(" ", ""))
    time.sleep(1)

# tags
pay_tag_list = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(1, 12):
    driver.get(pay+"page/{}".format(i))

    page = driver.find_element(By.CSS_SELECTOR, "body > div > main > div > div._listTemplate_aknty_21 > div > ul")
    articles = page.find_elements(By.TAG_NAME, "li")

    for article in articles:
        pay_tag = []
        title = article.find_element(By.TAG_NAME, "a")
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
        ActionChains(driver).move_to_element(article).click(title).perform()
        driver.implicitly_wait(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        tags = soup.find_all("a", "tag astro-WAKMUXVF")
        for tag in tags:
            pay_tag.append(tag.text)
        pay_tag_list.append(list(pay_tag))

        driver.back()

# to_csv
pay_df = pd.DataFrame({'title':pay_title, 'date':pay_date, 'tags':pay_tag_list, 'company':'카카오페이', 'link':pay_link})
pay_df.to_csv("kakao_pay.csv", index=False)