import pandas as pd

past = pd.read_csv('C:/Users/lexsh/Desktop/pastStock/A000660_pastStock.csv')  # 과거데이터 읽음
del past["date"]
del past["time"]
past = past.values.tolist()  # 이중리스트
now = pd.read_csv('C:/Users/lexsh/Desktop/pastStock/nowData.csv')  # 실시간데이터

del now["time"]
now = now.values.tolist()

for i in range(0,len(now)):
    past.append(now[i])
past = past[-30:]
print(past)
