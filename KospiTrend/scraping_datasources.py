from bs4 import BeautifulSoup
from numpy import inner
from pandas import DataFrame
import pandas as pd
import matplotlib.pylab as plt


# ========================== 데이타 스크래핑 ===================================

# http://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1080
# 테이블에서 월별 코스피 지수 (1997-2021년) 스크래핑 (292개)
table_k = BeautifulSoup(open('./htmlsource/kospiIndex_1997-2021.html','r',encoding='utf-8').read()).get_text()
kospiIndex = table_k.split('\n')[2:294]

# http://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1073
# 테이블에서 5년물 국고채 금리 스크래핑 (292개)
table_b5 = BeautifulSoup(open('./htmlsource/bondRate(5y).html',encoding='utf-8').read()).get_text()
bondRate_5year = table_b5.split('\n')[2:294]

# 테이블에서 10년물 국고채 금리 스크래핑 (292개)
table_b10 = BeautifulSoup(open('./htmlsource/bondRate(10y).html',encoding='utf-8').read()).get_text()
bondRate_10year = table_b10.split('\n')[2:294]

# 한국은행 기준금리 스크래핑
table_b = BeautifulSoup(open('./htmlsource/bondRate(b).html',encoding='utf-8').read()).get_text()
bondRate_b = table_b.split('\n')[2:294]

# http://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068
# 환율정보 스크래핑 (2000~2020): 256개
table_c = BeautifulSoup(open('./htmlsource/exchangeRate.html',encoding='utf-8').read()).get_text()
exchRate = table_c.split('\n')[2:258]

# GDP성장율 스크래핑
table_gdp = BeautifulSoup(open('./htmlsource/gdpR_kr.html',encoding='utf-8').read()).get_text()
gdp_d = table_gdp.split('\n')[2:246]

# GDP 스크래핑
table_gdp = BeautifulSoup(open('./htmlsource/gdp_kr.html',encoding='utf-8').read()).get_text()
gdp_n = table_gdp.split('\n')[2:246]

# 코스피 시가총액 스크래핑
table_komc = BeautifulSoup(open('./htmlsource/kospiMarketCap.html',encoding='utf-8').read()).get_text()
kmc = table_komc.split('\n')[2:306]



# vix지수 스크래핑
table_vixhtml = BeautifulSoup(open('C:/Github/tutorial/htmlsource/VixIndex.html',encoding='utf-8').read()).get_text()
table_vixhtml = table_vixhtml.split('\n')[1:1808]
table_vixhtml = list(filter(None,table_vixhtml))
# 년도/월 스크래핑
vix_m = []
for i in table_vixhtml:
    a = i.find("년")
    if a == 4:
        vix_m.append(i)

vix_ym = []
for j in vix_m:
    x = j[:4]
    if len(j)==8:
        s = "0" + j[5:7].strip()
        u = x + s
        vix_ym.append(u)
    elif len(j)==9:
        u = x + j[6:8].strip()
        vix_ym.append(u)

# vix 데이타 추출
vix_d = []
rn = []
a = 1
for i in range(1,259):
    rn.append(a)
    a = a + 6

for i in rn:
    c = table_vixhtml[i]
    vix_d.append(c)





# ==============================년월 column 스크래핑======================================

# 테이블에서 년도-월 스크래핑 (292개)
table_m = BeautifulSoup(open('./htmlsource/bondMonth.html','r',encoding='utf-8').read()).get_text()
yearMonth_t = table_m.split('\n')[3:295]

# '월' 제외
yearMonth = []
for i in yearMonth_t:
    t = i[:6]
    yearMonth.append(t)

# 환율정보 테이블의 '년월' 스크래핑
table_em = BeautifulSoup(open('./htmlsource/ExMonth.html',encoding='utf-8').read()).get_text()
yearMonth_et = table_em.split('\n')[3:259]
yearMonth_ex = []
for i in yearMonth_et:
    t = i[:6]
    yearMonth_ex.append(t)

# GDP성장율 년월 추출
table_gdp_m = BeautifulSoup(open('./htmlsource/gdpR_kr_year.html',encoding='utf-8').read()).get_text()
gdp_m = table_gdp_m.split('\n')[3:247]
yearmonth_gdp = []
for i in gdp_m:
    period_slice = i[4:]
    if period_slice == '1/4':
        rep = i.replace('1/4','02')
        yearmonth_gdp.append(rep)
    elif period_slice == '2/4':
        rep =i.replace('2/4','05')
        yearmonth_gdp.append(rep)
    elif period_slice == '3/4':
        rep =i.replace('3/4','08')
        yearmonth_gdp.append(rep)
    elif period_slice == '4/4':
        rep =i.replace('4/4','11')
        yearmonth_gdp.append(rep)

# 코스피 시가총액 년월 스크래핑
table_komc_m = BeautifulSoup(open('./htmlsource/kospiCap_month.html',encoding='utf-8').read()).get_text()
km_m = table_komc_m.split('\n')[3:307]

yearMonth_km = []

for i in km_m:
    t = i[:6]
    yearMonth_km.append(t)


# ============================= 데이타 리스트 ==================================
# 데이타(코스피지수,금리)
tbldata_k = {
    'year-month':yearMonth, 
    'KospiIndex':kospiIndex,
    'bondRate(5)':bondRate_5year,
    'bondRate(10)':bondRate_10year,
    'bondRate(b)':bondRate_b
}
# 데이타(환율)
tbldata_e = {
    'year-month':yearMonth_ex,
    'ExchangeRate':exchRate
}
# 데이타(GDP)
tbldata_g = {
    'year-month':yearmonth_gdp,
    'GDP growth':gdp_d,
    'Nominal GDP':gdp_n
}
# 데이타(코스피 시가총액)
tbldata_kc = {
    'year-month':yearMonth_km,
    'Kospi market cap':kmc
}

tbldata_vix = {
    'year-month':vix_ym,
    'Vix indicator':vix_d
}


# =======================================데이타 프레임=================================

# 데이타프레임(코스피/금리)
df_k = DataFrame(tbldata_k)
# 데이타프레임(환율)
df_e = DataFrame(tbldata_e)
# 데이타프레임(GDP성장율) 
df_g = DataFrame(tbldata_g)
# 데이타프레임(코스피 시가총액) 
df_kc = DataFrame(tbldata_kc)
# 데이타프레임(Vix지수)
df_v = DataFrame(tbldata_vix)

# # (참조코드)
# # df_g = pd.DataFrame.from_dict(tbldata_g, orient='index')
# # df_gd = df_g.transpose()
# # print(len(df_gd))
# # print(df_gd)


# =====================================테이블 병합 ============================
df_1 = pd.merge(df_k,df_e,how='left')
df_2 = pd.merge(df_1,df_g,how='left')
df_3 = pd.merge(df_2,df_kc,how='left')
df_4 = pd.merge(df_3,df_v,how='left')
df_4 = df_4.set_index('year-month')
# df_3.to_csv('ksp_bond_exch_kmc.csv')
df_4.to_csv('ksp_bond_exch_kmc_vix.csv')
print(df_4)


