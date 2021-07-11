import time
import pandas as pd
from pandas.core.frame import DataFrame
from selenium import webdriver
import matplotlib.pyplot as plt

### 엑셀에서 종목코드 불러오기
xl = pd.read_excel(io='./stocks_mirae.xls', sheet_name='stock')
code = list(xl['종목번호'])
name = list(xl['종목명'])

code_list = []
stock_list = []

### '미래에셋'에서 받은 엑셀파일 종목명에서 한국주식만 추출 (6자리 code만 추출)
for i,j in zip(code,name):
    slice = i[1:]
    if len(slice) == 6:
        code_list.append(slice)
        stock_list.append(j)

print(code_list)
print(stock_list)

### 문자변환함수: 불러온 데이타에서 불필요한 문자제거하고, 문자를 숫자로 변환하기 위한 함수
def rep(txt):
    dic = {'조':'',',':'',' ':''}
    transTable = txt.maketrans(dic)
    txt = txt.translate(transTable)
    try:
        flt = float(txt)
        return flt
    except:
        return None

# 종목별 가져올 정보 설정
curr_price = []              # 현재가
market_cap = []              # 시가총액
sales_2018 = []              # 2018년 매출액
sales_2019 = []              # 2019년 매출액
sales_2020 = []              # 2020년 매출액
sales_2021 = []              # 2021년 예상매출액
opmargin_2018 = []           # 2018년 영업이익
opmargin_2019 = []           # 2019년 영업이익
opmargin_2020 = []           # 2020년 영업이익
opmargin_2021 = []           # 2021년 영업이익
netmargin_2018 = []          # 2018년 당기순이익
netmargin_2019 = []          # 2019년 당기순이익
netmargin_2020 = []          # 2020년 당기순이익
netmargin_2021 = []          # 2021년 당기순이익
debtrate_2018 = []           # 2018년 부채비율
debtrate_2019 = []           # 2019년 부채비율
debtrate_2020 = []           # 2020년 부채비율
debtrate_2021 = []           # 2021년 부채비율
per_2018 = []                # 2018년 per
per_2019 = []                # 2019년 per
per_2020 = []                # 2020년 per
per_2021 = []                # 2021년 per
pbr_2018 = []                # 2018년 pbr
pbr_2019 = []                # 2019년 pbr
pbr_2020 = []                # 2020년 pbr
pbr_2021 = []                # 2021년 pbr
eps_2018 = []                # 2018년 eps
eps_2019 = []                # 2019년 eps
eps_2020 = []                # 2020년 eps
eps_2021 = []                # 2021년 eps

list = [
    curr_price,
    market_cap,
    sales_2018,
    sales_2019,
    sales_2020,
    sales_2021,
    opmargin_2018,
    opmargin_2019,
    opmargin_2020,
    opmargin_2021,
    netmargin_2018,
    netmargin_2019,
    netmargin_2020,
    netmargin_2021,
    debtrate_2018,
    debtrate_2019,
    debtrate_2020,
    debtrate_2021,
    per_2018,
    per_2019,
    per_2020,
    per_2021,
    pbr_2018,
    pbr_2019,
    pbr_2020,
    pbr_2021,
    eps_2018,
    eps_2019,
    eps_2020,
    eps_2021,

]

info = [
    'currprice',
    'macap',
    'sales2018',
    'sales2019',
    'sales2020',
    'sales_2021',
    'opmargin2018',
    'opmargin2019',
    'opmargin2020',
    'opmargin2021',
    'netmargin2018',
    'netmargin2019',
    'netmargin2020',
    'netmargin2021',
    'detrate2018',
    'detrate2019',
    'detrate2020',
    'detrate2021',
    'per2018',
    'per2019',
    'per2020',
    'per2021',
    'pbr2018',
    'pbr2019',
    'pbr2020',
    'pbr2021',
    'eps2018',
    'eps2019',
    'eps2020',
    'eps2021',
]

# 웹스크랩을 위한 css selector
selector = [
    '#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)',
    '#_market_sum',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td.t_line.cell_strong',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(2) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(2) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(2) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(2) > td.t_line.cell_strong',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td.t_line.cell_strong',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(7) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(7) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(7) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(7) > td.null.t_line.cell_strong',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(11) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(11) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(11) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(11) > td.t_line.cell_strong',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(13) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(13) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(13) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(13) > td.t_line.cell_strong',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(10) > td:nth-child(2)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(10) > td:nth-child(3)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(10) > td:nth-child(4)',
    '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(10) > td.t_line.cell_strong',
]

### 웹페이지 열기 및 데이타 가져오기
path = './chromedriver.exe'
drive = webdriver.Chrome(path)

for i in code_list:
    url = 'https://finance.naver.com/item/main.nhn?code='+ i
    drive.get(url)
    time.sleep(2)

    for i,j,k in zip(info,selector,list):
        i = drive.find_element_by_css_selector(j).text
        i = rep(i)
        k.append(i)

drive.close()


### 데이타프레임을 만들기 위한 dictionary
stock_info = {
    '종목명':stock_list,
    '현재가':curr_price,
    '시가총액':market_cap,
    '2018년 매출액':sales_2018,
    '2019년 매출액':sales_2019,
    '2020년 매출액':sales_2020,
    '2021년 매출액':sales_2021,
    '2018년 영업이익':opmargin_2018,
    '2019년 영업이익':opmargin_2019,
    '2020년 영업이익':opmargin_2020,
    '2021년 영업이익':opmargin_2021,
    '2018년 당기순이익':netmargin_2018,
    '2019년 당기순이익':netmargin_2019,
    '2020년 당기순이익':netmargin_2020,
    '2021년 당기순이익':netmargin_2021,
    '2018년 부채비율':debtrate_2018,
    '2019년 부채비율':debtrate_2019,
    '2020년 부채비율':debtrate_2020,
    '2021년 부채비율':debtrate_2021,
    '2018년 per':per_2018,
    '2019년 per':per_2019,
    '2020년 per':per_2020,
    '2021년 per':per_2021,
    '2018년 pbr':pbr_2018,
    '2019년 pbr':pbr_2019,
    '2020년 pbr':pbr_2020,
    '2021년 pbr':pbr_2021,
    '2018년 eps':eps_2018,
    '2019년 eps':eps_2019,
    '2020년 eps':eps_2020,
    '2021년 eps':eps_2021,
}

df = DataFrame(stock_info)
df.to_csv("stock_information.csv",encoding="cp949")



