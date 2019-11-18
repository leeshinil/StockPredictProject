import win32com.client
import datetime
import pandas as pd

# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()

# 현재가 객체 구하기
objStockMst2 = win32com.client.Dispatch("DsCbo1.StockMst2")
objStockMst2.SetInputValue(0, 'A005930,A000660,A035420,A017670,A006400,'
                              'A018260,A003550,A036570,A035720,A251270')
# IT관련기업 시가총액 TOP10
# 1. 삼성전자 005930
# 2. SK하이닉스 000660
# 3. NAVER 035420
# 4. SK텔레콤 017670
# 5. 삼성SDI 006400
# 6. 삼성에스디에스 018260
# 7. LG 003550
# 8. 엔씨소프트 036570
# 9. 카카오 035720
# 10. 넷마블 251270
objStockMst2.BlockRequest()

# 현재가 통신 및 통신 에러 처리
rqStatus2 = objStockMst2.GetDibStatus()
one_minute_later = ((datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%H%M')) #00초의 분의 값을 one_minute_later변수에 선언

time=[]
trade=[]
stock=[]
pastTrade=[]
for i in range(10):
    trade.append([])
    stock.append([])
    pastTrade.append([])

# 현재가 정보 조회
if (objStockMst2.GetDataValue(2, 0) >= int('0800') and objStockMst2.GetDataValue(2, 0) <= int('1530') # 현재시간이 8시부터 15시30분까지 수집을 함(장 시간)
        and rqStatus2 == 0):
    print("장이 열렸습니다")
    print("현재가 통신 OK")
    while True:
        nowTime = datetime.datetime.now().strftime('%H%M') #현재시간 시간 분을 제외한 00초에 nowTime변수에 저장
        if (nowTime == one_minute_later): # nowTime이 one_minute_later랑 같을 때 데이터 수집
            for i in range(0, 10):
                pastTrade[i].append(objStockMst2.GetDataValue(11, i))
            objStockMst2.SetInputValue(0, 'A005930,A000660,A035420,A017670,A006400,'
                                          'A018260,A003550,A036570,A035720,A251270')
            objStockMst2.BlockRequest()
            time.append(nowTime)
            for i in range(0, 10): #회사 10개
                trade[i].append(objStockMst2.GetDataValue(11, i) - pastTrade[i][-1])  # 거래량
                stock[i].append(objStockMst2.GetDataValue(3, i))  # 현재가
                print("종목명: ", objStockMst2.GetDataValue(1,i))
                print(" 시간 , 거래량 , 현재가 ")
                print(time, trade[i], stock[i])
                print()
                df = pd.DataFrame(columns=['time', 'tradevolume', 'stock'])
                df["time"] = time
                df["tradevolume"] = trade[i]
                df["stock"] = stock[i]
                if i==0:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A005930_now.csv", mode='w', header=True, index=False)
                elif i==1:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A000660_now.csv", mode='w', header=True, index=False)
                elif i==2:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A035420_now.csv", mode='w', header=True, index=False)
                elif i==3:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A017670_now.csv", mode='w', header=True, index=False)
                elif i==4:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A006400_now.csv", mode='w', header=True, index=False)
                elif i==5:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A018260_now.csv", mode='w', header=True, index=False)
                elif i==6:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A003550_now.csv", mode='w', header=True, index=False)
                elif i==7:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A036570_now.csv", mode='w', header=True, index=False)
                elif i==8:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A035720_now.csv", mode='w', header=True, index=False)
                elif i==9:
                    df.to_csv("C:/Users/lexsh/Desktop/server/A251270_now.csv", mode='w', header=True, index=False)
            one_minute_later = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%H%M') # now시간을 00초가 됐을때 one_minute_later에 선언
else:
    print("장이 닫혔습니다")
    print(rqStatus2)
    exit()