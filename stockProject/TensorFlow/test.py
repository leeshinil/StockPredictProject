import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
import datetime

data = pd.read_csv('C:/Users/lexsh/Desktop/pastStock/A000660.csv')
# print(data.head())

stock = data['stock'].values

seq_len = 100
sequence_length = seq_len +1
result = []
for index in range(len(stock)-sequence_length):
    result.append(stock[index:index+sequence_length])

normalized_data = []

for window in result:
    normalized_window = [((float(window[0]/float(p)))-1) for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

print(result)

row = int(round(result.shape[0] * 0.9999))
train = result[:row,:]
np.random.shuffle(train)

x_train = train[:,:-1]
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
y_train = train[:,-1]


x_test = result[row:,:-1]
# print(x_test)
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
y_test = result[row:,-1]
# print(x_test)
# print(x_train.shape)
# print(x_test.shape)

model = Sequential()

model.add(LSTM(50, return_sequences=True, input_shape=(100,1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1,activation='linear'))

model.compile(loss='mse', optimizer='rmsprop')

# print(model.summary())

model.fit(x_train,y_train,validation_data=(x_test,y_test), batch_size=500,epochs=2)#학습시키는것.

pred= model.predict(x_test)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(y_test,label='True')
ax.plot(pred,label='Prediction')
ax.legend()
plt.show()