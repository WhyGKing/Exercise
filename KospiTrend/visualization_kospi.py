import pandas as pd
import matplotlib.pylab as plt
import numpy as np

# 파일에서 자료호출 
df = pd.read_csv('ksp_bond_exch_kmc_vix.csv')
# 추가자료검토필요: 수출입자료, vix지수, 소비자/생산자 물가지수, 
# 연준금리, 고용지표, 미국10년물국채금리, PMI, 내구재 주문량, ISM제조업지수


# 데이타 자료타입 변경
df["KospiIndex"]=df["KospiIndex"].str.replace(',','')
df["ExchangeRate"]=df["ExchangeRate"].str.replace(',','')
df["Nominal GDP"]=df["Nominal GDP"].str.replace(',','')
df["Kospi market cap"]=df["Kospi market cap"].str.replace(',','')

df['bondRate(10)'] = pd.to_numeric(df['bondRate(10)'],errors='coerce')
df['ExchangeRate'] = pd.to_numeric(df['ExchangeRate'],errors='coerce')
df['KospiIndex'] = pd.to_numeric(df['KospiIndex'],errors='coerce')
df['Nominal GDP'] = pd.to_numeric(df['Nominal GDP'],errors='coerce')
df['Kospi market cap'] = pd.to_numeric(df['Kospi market cap'],errors='coerce')
df['Vix indicator'] = pd.to_numeric(df['Vix indicator'],errors='coerce')
df['year-month'] = df['year-month'].astype(str)

df['Buffet indicator'] = df['Kospi market cap']*1000 / df['Nominal GDP']
df['Vix Ind x 10'] = df['Vix indicator'] * 10


# 각 열 변수 지정
x1 = df['bondRate(10)']
x2 = df['bondRate(5)']
x3 = df['ExchangeRate']
x4 = df['year-month']
y1 = df['KospiIndex']
y2 = df['GDP growth']
y3 = df['Nominal GDP']
y4 = df['Kospi market cap']
y5 = df['Buffet indicator']

y7 =df['Vix indicator']
y8 = df['Vix Ind x 10']



# ====================================그래프 생성/서식설정========================================

# 코스피지수, 환율 그래프
fig,ax1 = plt.subplots()
line1 = ax1.plot(x4,y1, color='red',label='Kospi index')
line2 = ax1.plot(x4,x3, color='blue',label='Exchange rate',alpha=0.4)
line7 = ax1.plot(x4,y8, color='pink',label='Vix indicator x 10',alpha=0.7)

plt.xticks(fontsize=8,rotation=50)
plt.grid(True, alpha=0.3)


# ============================ 설명텍스트 추가 ==================================
# 주용 경제사건 메모/ 텍스트 삽입
month = ['200003', # 닷컴 버블 붕괴시작
         '200109', # 911테러 발생
         '200112', # 엔론사 파산         
         '200406', # Fed 금리인상 시작
         '200704', # 서브프라임 모기지 사태
         '200809', # 리먼브라더스 파산
         '200903', # 1차 양적완화
         '201004', # 그리스 구제금융신청
         '201011', # 2차 양적완화
         '201104', # ECU Rate hike, s&p 미국 신용등급 하향조정, 소비자신뢰지수 하락
         '201401', # 연준 테이퍼링 실시
         '201512', # 연준 금리 인상 (0.0% -> 0.25%)
         '201606', # 영국 EU탈퇴
         '201801', # 트럼프 관세, 미중 무역분쟁 시작
         '202003', # 코로나 펜데믹선언
]

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
         'Fed tapering start',
         'Fed Rate hike (0.0 -> 0.25%)',
         'Brexit',
         'Trump tariffs:Trade war',
         'Corona pandemic'
]


ylocStart = [1000, 450, 800, 700, 1700, 1500, 1000, 1600, 1800, 2200, 2100, 1900, 2050, 2600, 2100  ] 
ylocEnd = [1700, 150, 1400, 400, 3000, 2800, 600, 1250, 1400, 2600, 2400, 1400, 2300, 2900, 2500   ]

date = []
for i in x4:
   date.append(i)

for i,j,k,l in zip(month, event, ylocStart, ylocEnd):
   locM = date.index(i)
   plt.annotate(j, xy=(locM, k), xytext=(locM, l),
   arrowprops={
       'facecolor':'r',
       'alpha': 0.5,
       'width': 3,
       'headwidth': 7       
       })



# 그래프 구간 음영설정
firstRiseStart = date.index('200303')
firstRiseEnd = date.index('200710')
secondRiseStart = date.index('200902')
secondRiseEnd = date.index('201104')
thirdRiseStart = date.index('202003')
thirdRiseEnd = date.index('202104')

plt.fill([firstRiseStart,firstRiseStart,firstRiseEnd,firstRiseEnd],[0,4000,4000,0],color='pink',alpha=0.3)
plt.fill([secondRiseStart,secondRiseStart,secondRiseEnd,secondRiseEnd],[0,4000,4000,0],color='pink',alpha=0.3)
plt.fill([thirdRiseStart,thirdRiseStart,thirdRiseEnd,thirdRiseEnd],[0,4000,4000,0],color='pink',alpha=0.3)


ax2 = ax1.twinx()
line3 = ax2.plot(x4,x1, color='purple',label='10year Treasury yield',alpha=0.4)
line4 = ax2.bar(x4,y2, color='black',label='GDP Growth rate',alpha=0.15)
line5 = ax2.plot(x4,y5, color='black',label='Buffett Indicator',alpha=0.4)


ax1.set_ylabel('KRW') # -------------------------------------------------------- 숫자 3자리수 쉼표 표시 어떻게?
ax1.set_ylim([0,4000])


ax2.set_ylabel('%')

# 한글입력 시도 ---------------------------------------------------------------- 잘안됨.
# font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
# plt.rc('font', family='NanumGothic')

ax1.xaxis.set_major_locator(plt.MaxNLocator(50)) # 코딩 위치가 중요함.


# 범례표시
lines = line1 + line2 + line3 + line7
labels = [ l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')
ax2.legend(line4,['GDP Growth rate'],loc='upper left')



# =======================================================================================

# 일정구간 확대해서 보기
# ax2.set_xlim(['201701','202104'])

# 만든 사람을 표시하기 위한 텍스트 상자
plt.text(280, -10.5, 'by WhyG',fontsize=10)

# 그래프 출력
plt.show()


# 그래프 저장
# plt.savefig('kospi_1.png')
