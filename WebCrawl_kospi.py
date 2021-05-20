
####< 통계청 홈페이지에서 1976년부터 2020년까지의 Kospi지수를 Dataframe을 생성하기 위한 코드입니다. >####

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# ************************************************ 2차 시도 ******************************************************

# 웹페이지 개발자도구에서 table 해당부분의 html을 복사해서 새파일 생성해서 저장-->파일불러와서 Beatifulsoup으로 parsing해서 list생성
# 웹페이지: http://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1080

table_k = BeautifulSoup(open('C:/Github/Exercise/src_kospi.html','r',encoding='utf-8').read()).get_text()
kospiIndex = table_k.split('\n')[1:497]

table_m = BeautifulSoup(open('C:/Github/Exercise/src_month.html','r',encoding='utf-8').read()).get_text()
month_d = table_m.split('\n')[3:499]

month = []

for i in month_d:
    strYear = i[:4]
    strYear += "년"
    strMonth = i[4:]
    dt = strYear + strMonth
    month.append(dt)

### 년도별 코스피지수 테이블 만들기
tbldata = {
    'year-month':month,    
    'KospiIndex':kospiIndex      
}
df = DataFrame(tbldata)
df_kospi_index = df.set_index("year-month")

print(df_kospi_index)

