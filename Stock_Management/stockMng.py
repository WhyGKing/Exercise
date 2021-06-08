import time
import pandas as pd
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

### 엑셀 불러오기
df = pd.read_excel(io='./stocks_mirae.xls', sheet_name='stock')
code = df['종목번호']
name = df['종목명']

### 종목코드 리스트 작성
code_li = []
for i in code:
    if len(i) == 7:
        slice = i[1:]
        code_li.append(slice)
    else:
        pass
# print(code_li)

### 종목명 리스트 작성
name_li = []
for i,j in zip(name,code):
    if len(j) == 7:
        name_li.append(i)
# print(name_li)


### url 불러오기
path = 'C:/Github/tutorial/stockMng/chromedriver.exe'
drive = webdriver.Chrome(path)
url = 'https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/stock/BIP_CNTS02006V.xml&menuNo=44'
drive.get(url)
time.sleep(3)

### 주식정보 리스트 작성
market_cap = []
No_stocks = []
curr_price = []

sales_vol2020 = []
sales_vol2019 =[]
sales_vol2018 = []
sales_vol2017 = []
op_income2020 = []
op_income2019 = []
op_income2018 = []
op_income2017 = []
net_income2020 = []
net_income2019 = []
net_income2018 = []
net_income2017 = []
capital2020 = []
capital2019 = []
capital2018 = []
capital2017 = []
debt_ratio2020 = []
debt_ratio2019 = []
debt_ratio2018 = []
debt_ratio2017 = []
per_2020 = []
per_2019 = []
per_2018 = []
per_2017 = []
pbr_2020 = []
pbr_2019 = []
pbr_2018 = []
pbr_2017 = []


### 종목별 주식/재무정보 추출
for i in code_li:
    drive.refresh()
    time.sleep(3)
    # 검색창 팝업
    drive.find_element_by_id('sn_group4').click()
    time.sleep(3)

    # 팝업창에서 종목선택/입력
    drive.switch_to_frame('iframe1')
    drive.find_element_by_id('search_string').send_keys(i)
    drive.find_element_by_id('P_group100').click()
    time.sleep(2)
    drive.find_element_by_id('P_isinList_0_P_ISIN_ROW').click()

    # 다시 메인화면으로 와서 선택된 종목 조회
    drive.switch_to_default_content()
    drive.find_element_by_id('group94').click()
    time.sleep(5)



    # 시가총액
    macap = drive.find_element_by_css_selector('#MARTP_TOTAMT').text
    market_cap.append(macap)
    # 총주식수
    stockno = drive.find_element_by_css_selector('#ISSU_SCHD_STKQTY').text
    No_stocks.append(stockno)

    # 현재가
    currprice = drive.find_element_by_css_selector('#LDAY_CPRI').text
    curr_price.append(currprice)
    # 매출액
    salesvol2020 = drive.find_element_by_css_selector('#grid5_cell_0_4 > nobr').text
    sales_vol2020.append(salesvol2020)
    salesvol2019 = drive.find_element_by_css_selector('#grid5_cell_0_3 > nobr').text
    sales_vol2019.append(salesvol2019)
    salesvol2018 = drive.find_element_by_css_selector('#grid5_cell_0_2 > nobr').text
    sales_vol2018.append(salesvol2018)
    salesvol2017 = drive.find_element_by_css_selector('#grid5_cell_0_1 > nobr').text
    sales_vol2017.append(salesvol2017)
    # 영업이익
    opincome2020 = drive.find_element_by_css_selector('#grid5_cell_1_4 > nobr').text
    op_income2020.append(opincome2020)
    opincome2019 = drive.find_element_by_css_selector('#grid5_cell_1_3 > nobr').text
    op_income2019.append(opincome2019)
    opincome2018 = drive.find_element_by_css_selector('#grid5_cell_1_2 > nobr').text
    op_income2018.append(opincome2018)
    opincome2017 = drive.find_element_by_css_selector('#grid5_cell_1_1 > nobr').text
    op_income2017.append(opincome2017)
    # 당기순이익
    netincome2020 = drive.find_element_by_css_selector('#grid5_cell_2_4 > nobr').text
    net_income2020.append(netincome2020)
    netincome2019 = drive.find_element_by_css_selector('#grid5_cell_2_3 > nobr').text
    net_income2019.append(netincome2019)
    netincome2018 = drive.find_element_by_css_selector('#grid5_cell_2_2 > nobr').text
    net_income2018.append(netincome2018)
    netincome2017 = drive.find_element_by_css_selector('#grid5_cell_2_1 > nobr').text
    net_income2017.append(netincome2017)
    # 자본총계
    cap2020 = drive.find_element_by_css_selector('#grid5_cell_7_4 > nobr').text
    capital2020.append(cap2020)
    cap2019 = drive.find_element_by_css_selector('#grid5_cell_7_3 > nobr').text
    capital2019.append(cap2019)
    cap2018 = drive.find_element_by_css_selector('#grid5_cell_7_2 > nobr').text
    capital2018.append(cap2018)
    cap2017 = drive.find_element_by_css_selector('#grid5_cell_7_1 > nobr').text
    capital2017.append(cap2017)
    # 부채비율
    debtr2020 = drive.find_element_by_css_selector('#grid5_cell_7_4 > nobr').text
    debt_ratio2020.append(debtr2020)
    debtr2019 = drive.find_element_by_css_selector('#grid5_cell_7_3 > nobr').text
    debt_ratio2019.append(debtr2019)
    debtr2018 = drive.find_element_by_css_selector('#grid5_cell_7_2 > nobr').text
    debt_ratio2018.append(debtr2018)
    debtr2017 = drive.find_element_by_css_selector('#grid5_cell_7_1 > nobr').text
    debt_ratio2017.append(debtr2017)
    # PER
    per2020 = drive.find_element_by_css_selector('#grid5_cell_7_4 > nobr').text
    per_2020.append(per2020)
    per2019 = drive.find_element_by_css_selector('#grid5_cell_7_3 > nobr').text
    per_2019.append(per2019)
    per2018 = drive.find_element_by_css_selector('#grid5_cell_7_2 > nobr').text
    per_2018.append(per2018)
    per2017 = drive.find_element_by_css_selector('#grid5_cell_7_1 > nobr').text
    per_2017.append(per2017) 
    # PBR
    pbr2020 = drive.find_element_by_css_selector('#grid5_cell_7_4 > nobr').text
    pbr_2020.append(pbr2020)
    pbr2019 = drive.find_element_by_css_selector('#grid5_cell_7_3 > nobr').text
    pbr_2019.append(pbr2019)
    pbr2018 = drive.find_element_by_css_selector('#grid5_cell_7_2 > nobr').text
    pbr_2018.append(pbr2018)
    pbr2017 = drive.find_element_by_css_selector('#grid5_cell_7_1 > nobr').text
    pbr_2017.append(pbr2017) 

stock_info = {
    'stock_name' : name_li,
    'sales_volume(2020)' : sales_vol2020,
    'sales_volume(2019)' : sales_vol2019,
    'sales_volume(2018)' : sales_vol2018,
    'sales_volume(2017)' : sales_vol2017,
    'operating_income(2020)' : op_income2020,
    'operating_income(2019)' : op_income2019,
    'operating_income(2018)' : op_income2018,
    'operating_income(2017)' : op_income2017,
    'net_income(2020)' : net_income2020,
    'net_income(2019)' : net_income2019,
    'net_income(2018)' : net_income2018,
    'net_income(2017)' : net_income2017,
    'capital(2020)' : capital2020,
    'capital(2019)' : capital2019,
    'capital(2018)' : capital2018,
    'capital(2017)' : capital2017,
    'debt_ratio(2020)' : debt_ratio2020,
    'debt_ratio(2019)' : debt_ratio2019,
    'debt_ratio(2018)' : debt_ratio2018,
    'debt_ratio(2017)' : debt_ratio2017,
    'PER(2020)' : per_2020,
    'PER(2019)' : per_2019,
    'PER(2018)' : per_2018,
    'PER(2017)' : per_2017,
    'PBR(2020)' : pbr_2020,
    'PBR(2019)' : pbr_2019,
    'PBR(2018)' : pbr_2018,
    'PBR(2017)' : pbr_2017
}

df = DataFrame(stock_info)
df.to_csv("stock_information.csv",encoding="cp949")


