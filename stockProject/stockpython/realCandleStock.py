#candleStock
# 1. 삼성전자 A005930
# 2. SK하이닉스 A000660
# 3. NAVER A035420
# 4. SK텔레콤 A017670
# 5. 삼성SDI A006400
# 6. 삼성에스디에스 A018260
# 7. LG A003550
# 8. 엔씨소프트 A036570
# 9. 카카오 A035720
# 10. 넷마블 A251270

import win32com.client
from pandas import Series, DataFrame
import pandas as pd
import csv
from datetime import datetime

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart") #StockChart 라이브러리 사용(대신증권 api)
yesterdayStock = int(datetime.today().strftime("%Y%m%d")) -1 #yesterdayStock변수에 어제 날짜를 선언

company = ["A005930","A000660","A035420","A017670","A006400","A018260","A003550","A036570","A035720","A251270"] # 10개 기업의 코드 이름을 company변수에 선언
for j in company: # company1번 부터 10까지 차례로 실행
    date = []
    start = []
    high = []
    low = []
    end = []
    #대신증권 라이브러리인 SetInpuValue를 사용하여 데이터 가져오기
    instStockChart.SetInputValue(0, j)
    instStockChart.SetInputValue(1, ord('1'))  # 날자로
    instStockChart.SetInputValue(2, yesterdayStock)  # 종료일
    instStockChart.SetInputValue(3, '20190101')  # 시작일
    instStockChart.SetInputValue(5, (0, 2, 3, 4, 5)) # 날짜/시가/고가/저가/종가
    instStockChart.SetInputValue(6, ord('D'))

    # BlockRequest
    instStockChart.BlockRequest()
    # GetHeaderValue
    numData = instStockChart.GetHeaderValue(3) #가져온 데이터 갯수
    print(numData)


    # GetDataValue
    #가져온 데이터 개수만큼 각 파트에 append
    for i in range(numData):
        date.append(instStockChart.GetDataValue(0, i))
        start.append(instStockChart.GetDataValue(1, i))
        high.append(instStockChart.GetDataValue(2, i))
        low.append(instStockChart.GetDataValue(3, i))
        end.append(instStockChart.GetDataValue(4, i))

    df = pd.DataFrame(columns= ['date', 'start', 'high', 'low', 'end'])
    df["date"] = date
    df["start"] = start
    df["high"] = high
    df["low"] = low
    df["end"] = end
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)
    print(df)
    df.to_csv("C:/Users/lexsh/Desktop/server/"+j+"_candle.csv", mode='w', header=True) #csv에 저장
