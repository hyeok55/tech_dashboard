import csv
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from wordcloud import WordCloud
from collections import Counter

from techblog.settings import STATIC_DIR
from pathlib import Path
import os

from .models import *

# 데이터 -> views.py에서 정의?

# data = Company_Tag.objects.values('company', 'tag', 'count')
# company = Company_Tag.objects.values('company')
# tag = Company_Tag.objects.values('tag')
# count = Company_Tag.objects.values('count')


# 전체 기업 태그 빈도수 barchart 
def all_tags():
    tag = Company_Tag.objects.values[:]['tag']
    count = Company_Tag.objects.values[:]['count']
    tag_df = pd.DataFrame(tag)
    count_df = pd.DataFrame(count)
    plt.title('전체 기업 태그 빈도수')
    plt.xlabel('빈도수')
    plt.ylabel('태그')
    sns.barplot(x=count_df, y=tag_df, palette='cubehelix')
    plt.savefig(os.path.join(STATIC_DIR, 'images/all.png'))


# 기업별 태그 빈도수 barchart - 상위 20
def company_tags(company):
    data = Company_Tag.objects.all().order_by('-count')[:20]
    tag = data.tag
    count = data.count
    tag_df = pd.DataFrame(list(tag))
    count_df = pd.DataFrame(list(count))
    plt.title(company)
    sns.barplot(x=count_df, y=tag_df, palette='cubehelix')
    plt.xlabel('빈도수')
    plt.ylabel('태그')
    plt.savefig(os.path.join(STATIC_DIR, 'images/{}.png'.format(company)))
