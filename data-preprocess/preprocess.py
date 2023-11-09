import pickle
import os
import pandas as pd
from tag_dictionary import tag_dict
from string import punctuation
import re

def replace_tag(ls):
    """
    tag 전처리 함수
    """
    if isinstance(ls, list):
        return "#".join(list(map(lambda x: tag_map.get(x.lower(), x.lower()), ls)))
    else:
        return ""
    
def replace_date(date):
    """
    date 전처리 함수
    20xx.xx.xx 형식으로 변환
    """
    if "-" in date:
        # 20xx-xx-xx 변환
        return date.replace("-", ".")
    if ". " in date:
        # 20xx. x(xx). x(xx). -> 20xx.x(xx).x(xx)
        date = date[:-1].replace(" ","")
        
    # 달을 숫자로 변환 하는 딕셔너리들
    month_dict1 = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
        } 
    month_dict2 = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    

    splited_date = date.split(".")
    if len(splited_date) == 3:
        if (len(splited_date[0]) == len(splited_date[1])) and (len(splited_date[0]) == len(splited_date[2])):
            # xx[year].xx[month].xx[day] 처리 
            # 예: 21.05.12 
            return "20" + date
        if len(splited_date[1]) == 1 or len(splited_date[2]) == 1:
            # 20xx.x(xx).x(xx) 처리
            result = date[:5]
            result += splited_date[1] + "." if len(splited_date[1]) == 2 else "0" + splited_date[1] + "."
            result += splited_date[2] if len(splited_date[2]) == 2 else "0" + splited_date[2]
            return result
        if len(splited_date[0]) == 3:
            # xxx[month].xx[day].20xx 처리 
            # 예: Mar.13.2022
            return splited_date[2] + "." + month_dict1[splited_date[0]] + "." + splited_date[1]
        return date

    # [month] [day], [year] 또는 [day] [month], [year]인 경우만 남음
    # 이때 2023년도는 ,[year]가 생략인 경우도 있음
    if len(date) <= 6:
        # 2023년도 중 ,[year]이 빠진 경우 형태를 맞춰줌
        # xxx[month] x(xx)[day] 또는 x(xx)[day] xxx[month] 인 경우
        # 예: Mar 13 -> Mar 13, 2023또는 13 Mar -> 13 Mar, 2023
        date += ", 2023"
        
    # [month] [day] [year] 또는 [day] [month] [year]형태로 바궈줌
    date = date.replace(",", "")

    splited_date = date.split()
    if len(splited_date[1]) == 3:
        # xx[day] xxx[month] 20xx[year]인 경우
        # 예: 01 Mar 2021
        return splited_date[2] + "." + month_dict1[splited_date[1]] + "." + splited_date[0]

    if len(splited_date[0]) == 3:
        # xxx[month] xx(x)[day] 20xx[year]인 경우
        # 예: Mar 1 2021 -> result = 2021.03.
        result = splited_date[2] + "." + month_dict1[splited_date[0]] + "."
    else:
        # [month] xx(x)[day] 20xx[year]인 경우
        # 예: March 1 2021 -> result = 2021.03.
        result = splited_date[2] + "." + month_dict2[splited_date[0]] + "."
    return result + splited_date[1] if len(splited_date[1]) == 2 else result + "0" + splited_date[1] 

# 크롤링한 데이터를 하나의 데이터프레임으로 조합    
file_list = [file for file in os.listdir("../data/") if file.endswith(".pkl")]

data = []

for file in file_list:
    with open("../data/" + file, "rb") as f:
        tmp = pickle.load(f)
        for i in range(len(tmp)):
            if tmp[i]["tags"] and tmp[i]["tags"][0].startswith("#"):
                tmp[i]["tags"] = list(map(lambda x:x[1:], tmp[i]["tags"]))
        data.extend(tmp)
        
tag_map = {}
for repr, ls in tag_dict.items():
    for tag in ls:
        tag_map[tag] = repr
        
sites1 = ["devocean", "kakao", "kakao_pay"]
sites2 = ["full_line_data", "kakaoenter_data", "naver_data", "skplanet_data", "socar_data"]

df1 = pd.DataFrame(
    {
        "title": [],
        "date": [],
        "tags": [],
        "company": [],
        "link": []
    }
)
df2 = pd.DataFrame(
    {
        "title": [],
        "date": [],
        "tags": [],
        "company": [],
        "link": []
    }
)
for site in sites1:
    df1 = pd.concat([df1, pd.read_csv(f"../data/{site}.csv")]).reset_index(drop=True)
for site in sites2:
    df2 = pd.concat([df2, pd.read_csv(f"../data/{site}.csv")]).reset_index(drop=True)

df1["tags"] = df1["tags"].apply(lambda x: x[2:-2].split("', '"))
df2["tags"] = df2["tags"].str.split(", ")

tb = pd.DataFrame(data)[["title", "pub_date", "tags", "company_name", "url"]]
tb.columns = ['title', 'date', 'tags', 'company', 'link']

# 전체 데이터프레임
df = pd.concat([tb, df1, df2]).reset_index(drop=True)

# tags와 date를 수정
df["tags"] = df["tags"].apply(replace_tag)
df["date"] = df["date"].apply(replace_date)

# csv 파일로 저장
for company in df["company"].unique():
    df.loc[df["company"] == company].to_csv(f"../data/{company}.csv", index=False, encoding = 'utf-8-sig')