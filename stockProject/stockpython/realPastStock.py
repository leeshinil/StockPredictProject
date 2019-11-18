#pastStock
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
import pandas as pd
from datetime import datetime

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
yesterdayStock = int(datetime.today().strftime("%Y%m%d")) -1

company = ["A005930","A000660","A035420","A017670","A006400","A018260","A003550","A036570","A035720","A251270"]
for j in company:

    endDate = yesterdayStock
    date=[]
    time=[]
    stock=[]
    trade=[]
    while int(endDate) >= 20190118: # endDate를 어제부터 2019년1월18일까지 모든 데이터를 수집
        str(endDate) # string 값으로 endDate 를 변경
        # SetInputValue
        instStockChart.SetInputValue(0, j)
        # instStockChart.SetInputValue(1, ord('2'))  # 개수로
        # instStockChart.SetInputValue(4, '6000') #개수
        instStockChart.SetInputValue(1, ord('1'))  # 날자로
        instStockChart.SetInputValue(2, endDate)  # 종료일
        instStockChart.SetInputValue(3, '20190101')  # 시작일
        instStockChart.SetInputValue(5, (0, 1, 5, 8))
        instStockChart.SetInputValue(6, ord('m'))
        # 날짜 시간 종가 거래량

        # BlockRequest
        instStockChart.BlockRequest()

        # GetHeaderValue
        numData = instStockChart.GetHeaderValue(3)
        # numField = instStockChart.GetHeaderValue(1)
        endDate = instStockChart.GetDataValue(0, 4998) - 1 # endDate를 이용하여 가져올수 있는 총 데이터 수가 5000개이므로 하루전부터 다시 while문 실행
        # GetDataValue
        for i in range(numData):
            date.append(instStockChart.GetDataValue(0, i))
            time.append(instStockChart.GetDataValue(1, i))
            trade.append(instStockChart.GetDataValue(3, i))
            stock.append(instStockChart.GetDataValue(2, i))

    df = pd.DataFrame(columns= ['date', 'time', 'tradevolume', 'stock'])
    df["date"] = date
    df["time"] = time
    df["stock"] = stock
    df["tradevolume"] = trade
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)
    print(df)
    df.to_csv("C:/Users/lexsh/Desktop/server/"+j+"_pastStock.csv", mode='w', header=True,index=False) #csv에 저장
