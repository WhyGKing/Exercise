import matplotlib.pylab as plt
import FinanceDataReader as fdr
import datetime


# 코스피 지수
krx = fdr.DataReader('KS11', '1997-01-01', '2021-08-20', exchange='KRX')
krx = krx['Close']

# S&P500 지수
sp = fdr.DataReader('US500', '1997-01-01', '2021-08-20')
sp = sp['Close']

# 환율
usdkrw = fdr.DataReader('USD/KRW', '1997-01-01')
usdkrw = usdkrw['Close']

# 하이일드 채권 스프레드 (High-Yield Bond Spread)
hybs = fdr.DataReader('BAMLH0A0HYM2', start='1997-01-01', data_source='fred')

# 그래프 그리기
fig,ax1 = plt.subplots()
line1 = ax1.plot(krx, color='red',linewidth=1.5,label='Kospi index')
line2 = ax1.plot(sp, color='blue',linewidth=1,label='S&P500')
# line3 = ax1.plot(usdkrw, color='olive',linewidth=0.7,label='KRW/USD')

ax2 = ax1.twinx()
# line4 = ax2.plot(usyt, color='aqua',linewidth=0.7,label='US10Y')
line4 = ax2.plot(hybs, color='olive',linewidth=0.7,label='High-Yield Bond spread')

# 범례표시
lines = line1 + line2 + line4
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

# 주용 경제사건 메모/ 텍스트 삽입
date_event_str = ['2000-03', # 닷컴 버블 붕괴시작
         '2001-09', # 911테러 발생
         '2001-12', # 엔론사 파산         
         '2004-06', # Fed 금리인상 시작
         '2007-04', # 서브프라임 모기지 사태
         '2008-09', # 리먼브라더스 파산
         '2009-03', # 1차 양적완화
         '2010-04', # 그리스 구제금융신청
         '2010-11', # 2차 양적완화
         '2011-04', # ECU Rate hike, s&p 미국 신용등급 하향조정, 소비자신뢰지수 하락
         '2014-01', # 연준 테이퍼링 실시
         '2015-12', # 연준 금리 인상 (0.0% -> 0.25%)
         '2018-01', # 트럼프 관세, 미중 무역분쟁 시작
         '2020-03', # 코로나 펜데믹선언
]

date_event = []
for i in date_event_str:
    month = datetime.datetime.strptime(i, '%Y-%m')
    date_event.append(month)

event = ['Dotcom bubble burst',
         '911 attacks',
         'Enron bankrupt',        
         'Fed Rate hike start',
         'Subprime Mortgage Crisis',
         'Lehman Brothers bankrupt',
         'Fed 1st Quantitative easing',
         'Greece IMF bailout',
         'Fed QE2',
         'ECU Rate hike',
         'Fed tapering',
         'Fed Rate hike \n(0.0 -> 0.25%)',
         'Trump tariffs: \nTrade war',
         'Corona pandemic'
]

              #1   #2    #3   #4   #5   #6   #7   #8   #9    #10     #11   #12   #13  #14
yloc_start = [4.5, 10.5, 3.8, 3.9, 8.5, 5.0, 4.1, 5.2, 10.5, 11.6,   10.7, 11.2, 14.7, 17]
yloc_end =   [2.0,  12,  2.3, 2.3, 15,  1.8, 2.3, 3.0, 14,   13.4,   12,   15,   17,   20]


for i,j,k,l in zip(event,range(len(date_event)),yloc_start,yloc_end):
    plt.annotate(i,xy=(date_event[j], k), xytext=(date_event[j], l),
    arrowprops={
        'facecolor':'r',
        'alpha': 0.5,
        'width': 3,
        'headwidth': 7
        })

plt.grid(True,alpha=0.3)
plt.show()


