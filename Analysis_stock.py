### 코스피 지수와 국고채 장/단기 금리들간의 상관관계를 보기 위해 엑셀의 데이타를 불러와서 분석합니다.

import pandas as pd
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# 엑셀데이타 호출
xl = pd.read_excel(io='C:/Github/Exercise/bond_stock_timeseries.xlsx',sheet_name='Sheet1')

# 코스피 지수 열의 값에 천단위 구분 쉼표를 제거
xl["KospiIndex"]=xl["KospiIndex"].str.replace(',','')

# 데이타 타입이 문자열로 저장이 되어 있어, 실수(float)타입으로 변환
xl['ProfitRate(10)'] = pd.to_numeric(xl['ProfitRate(10)'],errors='coerce')
xl['KospiIndex'] = pd.to_numeric(xl['KospiIndex'],errors='coerce')

# 데이타가 없는 행을 제거한다.
xl = xl.dropna(how='any')

# 상관관계를 보기 위해 상관계수 산출
print(xl.corr())

# 상대적으로 상관관계가 높다고 판단되는 값들간의 산점도를 표시한다.
plt.scatter( xl['ProfitRate(10)'], xl['KospiIndex'], label = "data")
plt.xlabel('Bond rate(10)')
plt.ylabel('Kospi Index')
plt.show()



