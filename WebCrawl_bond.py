### 국채금리 변동자료를 받아오기 위한 코드입니다.

from typing import Text
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame

### 자바스크립트 url을 찾아서 주소를 가져옴.
source = requests.get('https://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=107301&idx_cd=1073&freq=M&period=199701:202104')
soup = BeautifulSoup(source.content,'html.parser')
table = soup.find('tbody').find('tr',{'id':'tr_107301_3'})
table5 = soup.find('tbody').find('tr',{'id':'tr_107301_5'})

### 국고채 10년물 금리와 콜금리 변동 자료 추출
td_all = table.find_all('td')
td_all5 = table5.find_all('td')

bond_data = []
for i in td_all:
    td_text = i.get_text()
    bond_data.append(td_text)

bond_data5 = []
for i in td_all5:
    td_text = i.get_text()
    bond_data5.append(td_text)


### 날짜(년월)를 추출하기 위해
th_date = soup.find('thead').find_all('th')

bond_month = []
for j in th_date: # 년도숫자 뒤에 '년'을 추가하고 싶은데, 못찾았음.
    th_d = j.get_text()
    strYear = th_d[:4]
    strYear += "년"
    strMonth = th_d[4:]
    th_d = strYear + strMonth
    bond_month.append(th_d)
del bond_month[0]

### 데이타프레임 만들기 (1997년1월~2021년4월)
tbldata = {
    'Year-Month':list(bond_month[:292]),    
    'ProfitRate(10)':list(bond_data[:292]),
    'ProfitRate(ca)':list(bond_data5[:292])
}
df = DataFrame(tbldata)
df_bond_rate = df.set_index("Year-Month")
print(df_bond_rate)






