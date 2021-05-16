### 통계청 홈페이지에서 1976년부터 2020년까지의 Kospi지수를 csv파일로 저장하기 위한 코드입니다.

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

### '통계청'홈페이지에서 데이타조회 페이지를 불러온다.
path = "C:\Github/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://kosis.kr/statHtml/statHtml.do?orgId=343&tblId=DT_343_2010_S0027')

### '시점' 탭의 '년' 체크박스 체크, '월' 체크박스 해제
element_tab = driver.find_element_by_xpath('//*[@id="tabTimeText"]/a/font').click()
element_checkBox = driver.find_element_by_id('checkM').click()
element_checkBox = driver.find_element_by_id('checkY').click()

### 드랍박스에서 '년도'선택
element_dropdown = driver.find_element_by_xpath('//*[@id="timeY"]/h2/select[1]')
select = Select(element_dropdown)
select.select_by_visible_text('1976')

### 조회버튼 클릭
element_tab = driver.find_element_by_class_name('rightBtn').click()


### JavaScript iframe으로 되어 있는 데이타를 불러올 수 있는가?
