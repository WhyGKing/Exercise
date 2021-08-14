from pykrx import stock
import FinanceDataReader as fdr
import time
import pandas as pd
import matplotlib.pyplot as plt

### 종목명 반환
def name_find(symbol_input,stock_symbol):
    try:
        for i in stock_symbol:
            if symbol_input == i:
                _name = stock_name[stock_symbol.index(i)]
        return _name
    except:
        print('종목코드 확인필요!')

### 종목코드 반환함수
def symbol_find(stock_input,stock_name):
    try:
        for i in stock_name:
            if stock_input == i:
                symbol = stock_symbol[stock_name.index(i)]
        return symbol
    except:
        print('종목명 확인필요!')

### 종목 또는 코드 리스트
def input_mod(input,stocks):
    if stocks.Name.isin(input).any():
        filtered = stocks.Name.isin(input)
        re = stocks[filtered].Symbol
    else:
        filtered = stocks.Symbol.isin(input)
        re = stocks[filtered].Symbol
    return re.values

### 전체종목목록 가져오기
stocks = fdr.StockListing('KRX')
stock_symbol = list(stocks['Symbol'])
stock_name = list(stocks['Name'])

### 종목명 또는 종목코드 입력
input_list = []

while True:
    write = input('종목명 또는 종목코드 입력: ')
    if write != '':
        input_list.append(write)
    else:
        break

### input 리스트에서 입력된 종목명을 종목코드로 바꾸기
for i in input_list:
    for j in stock_name:
        if i == j:
            symbol = symbol_find(i,stock_name)
            input_list[input_list.index(i)] = symbol

# # start_date = input('시작일: ')
# # end_date = input('종료일: ')

start_date = '20180601'
end_date = '20210813'

### 종목 재무정보
df_fundamental = []


for i in input_list:
    name = name_find(i,stock_symbol)
    print(name)
    
    df_fdm = stock.get_market_fundamental_by_date(start_date,end_date,i)
    df_fundamental.append(df_fdm)
    print(df_fdm)

    try:
        s_eps = df_fdm['PER']
    except:
        s_eps = pd.Series(0)
    try:
        s_bps = df_fdm['BPS']
    except:
        s_bps = pd.Series(0)
    try:
        s_pbr = df_fdm['PBR']
    except:
        s_pbr = pd.Series(0)

    mx_bps = max(s_bps.values)
    mn_bps = min(s_bps.values)
    mx_pbr = max(s_pbr.values)
    mn_pbr = min(s_pbr.values)

    ### 종목주가정보
    df_price = fdr.DataReader(i,start_date, end_date)
    s_price = df_price['Close']

    mx_price = max(s_price.values)
    mn_price = min(s_price.values)

    ### bps band 값 설정
    gab = (mx_pbr - mn_pbr)/3
    band0 = round(mx_pbr*1, 1)
    band1 = round(mx_pbr - gab, 1)
    band2 = round(mx_pbr - gab*2, 1)
    band3 = round(mn_pbr*1, 1)

    bpsband_0 = s_bps * band0
    bpsband_1 = s_bps * band1
    bpsband_2 = s_bps * band2
    bpsband_3 = s_bps * band3

    bpsband_0 = bpsband_0.to_frame()
    bpsband_0.columns= ['bpsband: {}'.format(band0)]
    bpsband_1 = bpsband_1.to_frame()
    bpsband_1.columns= ['bpsband: {}'.format(band1)]
    bpsband_2 = bpsband_2.to_frame()
    bpsband_2.columns= ['bpsband: {}'.format(band2)]
    bpsband_3 = bpsband_3.to_frame()
    bpsband_3.columns= ['bpsband: {}'.format(band3)]

    ### 차트생성 데이타 테이블
    df_chart = pd.concat([
        s_eps,
        s_price,
        bpsband_0,
        bpsband_1,
        bpsband_2,
        bpsband_3,
        ],
        axis=1
    )

    ### 차트 생성
    fig, ax1 = plt.subplots()
    line_price = ax1.plot(df_chart.index,df_chart['Close'],color='red',label='price')
    line_band00 = ax1.plot(df_chart.index,bpsband_0,label='band {}'.format(band0))
    line_band01 = ax1.plot(df_chart.index,bpsband_1,label='band {}'.format(band1))
    line_band02 = ax1.plot(df_chart.index,bpsband_2,label='band {}'.format(band2))
    line_band03 = ax1.plot(df_chart.index,bpsband_3,label='band {}'.format(band3))

    ax2 = ax1.twinx()
    line_per = ax2.plot(df_chart.index,df_chart['PER'],label='PER',color='aqua')

    lines = line_price + line_band00 + line_band01 + line_band02 + line_band03 + line_per

    labels = [l.get_label() for l in lines]

    ax1.legend(lines, labels, loc='upper left')
    plt.title(name,loc='center', fontsize=15,pad=20)

    ax1.set_ylabel('KRW')
    ax2.set_ylabel('PER')
   
plt.show()
