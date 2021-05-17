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


### 국고채 10년물 금리변동 자료 추출
td_all = table.find_all('td')

bond_data = []
for i in td_all:
    td_text = i.get_text()
    bond_data.append(td_text)
    

### 날짜(년월)를 추출하기 위해
th_date = soup.find('thead').find_all('th')

bond_month = []
for j in th_date: # 년도숫자 뒤에 '년'을 추가하고 싶은데, 못찾았음.
    th_d = j.get_text()
    bond_month.append(th_d)

### 데이타프레임 만들기 
df_rate = {'bond_10':bond_data}
df_bond_rate = DataFrame(df_rate)
print(df_bond_rate)
# index로 년월(bond_month)을 사용하고 싶은데 잘 안됨.







