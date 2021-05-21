from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

# 'https://www.professionalplastics.com/TRADENAMELIST'

soup = BeautifulSoup(open('C:/Github/Exercise/PolymerResin.html','r',encoding='utf-8').read())

# print(soup)
TradeName = []
Material = []
Manufacturer = []

t = int(len(soup.find_all('tr')))

for a in range(0,t):
    if a <= t:
        tr = soup.find_all('tr')[a]
        td_0 = tr.find_all('td')[0]
        tdt_0 = td_0.get_text()
        td_1 = tr.find_all('td')[1]
        tdt_1 = td_1.get_text()
        td_2 = tr.find_all('td')[2]
        tdt_2 = td_2.get_text()
        TradeName.append(tdt_0)
        Material.append(tdt_1)
        Manufacturer.append(tdt_2)
    a += 1

tbldata = {
    'TradeName':TradeName,
    'Material':Material,
    'Manufacturer':Manufacturer    
}
df = DataFrame(tbldata)
print(df)