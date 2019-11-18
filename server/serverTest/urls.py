from . import views
from django.urls import path
import subprocess
import tensorflow as tf
import csv
import pandas as pd
import numpy as np
import threading
import os
from datetime import datetime

def thread_run():
    threading.Timer(1,thread_run).start()
    company = ["A005930", "A000660", "A035420", "A017670", "A006400", "A018260", "A003550", "A036570", "A035720","A251270"]
    if datetime.now().second == 2:
        for i in company:
            combine(i)


def combine(i):
    past=pd.read_csv('C:/Users/lexsh/Desktop/server/'+ i +'_pastStock.csv')  # 과거데이터 읽음
    del past["date"]
    del past["time"]
    past=past.values.tolist()  #이중리스트

    if os.path.isfile('C:/Users/lexsh/Desktop/server/'+ i +'_now.csv'):
        file = open('C:/Users/lexsh/Desktop/server/'+ i +'_now.csv', "r")
        file_content = file.read()
        file.close()

        if file_content != "":
            now = pd.read_csv('C:/Users/lexsh/Desktop/server/'+ i +'_now.csv')  # 실시간데이터
            del now["time"]
            now = now.values.tolist()
            for j in range(0, len(now)):
                past.append(now[j])
            past = past[-30:]
            print(past)
            predict(past, i)
        else:
            print("nothing in here")
    else:
    	print("file is not here")


def predict(past, i):	
    tf.reset_default_graph()
    test = np.asarray(past, dtype=np.float64)
    min = np.min(test, 0)
    max = np.max(test, 0)


    def MinMaxScaler(data):
        numerator = data - min
        denominator = max - min
        # noise term prevents the zero division
        return numerator / (denominator + 1e-7)

    def MaxMinScaler(data):
        return data * ( max - min) + min
    # test = test[::-1]#역순

    testX = MinMaxScaler(test)
    # train Parameters
    seq_length = 30                                 # sequence = 30
    data_dim = 2                                    # input data는 한번에 들어감
    hidden_dim = 10                                 # 10개 hidden 있을 것.
    output_dim = 1                                  # output = 1
    learning_rate = 0.01
    iterations = 500

    # input place holders
    X = tf.placeholder(tf.float32, [None, seq_length, data_dim]) # None = batch_size
    Y = tf.placeholder(tf.float32, [None, 1])

    # build a LSTM network
    cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
    outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
    Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], output_dim, activation_fn=None)  # output은 마지막 하나만 쓰겠다

    # cost/loss
    loss = tf.reduce_sum(tf.square(Y_pred - Y))  # sum of the squares

    # optimizer
    optimizer = tf.train.AdamOptimizer(learning_rate)
    train = optimizer.minimize(loss)

    # RMSE
    targets = tf.placeholder(tf.float32, [None, 1])
    predictions = tf.placeholder(tf.float32, [None, 1])
    rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))
    saver = tf.train.Saver()
    sess = tf.Session()
    saver.restore(sess, 'C:/Users/lexsh/Desktop/server/'+ i +'-model')                         # 지정한 cehckpoint 변수값 복구
    test_predict = sess.run(Y_pred, feed_dict={X: [testX]})
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
    hour = datetime.now().hour
    minute = datetime.now().minute
    minute = minute + 1
    if minute == 60:
        hour = hour + 1
        minute = 00
    t = str(hour) + str(minute)

    f = open("C:/Users/lexsh/Desktop/server/"+ i +"_predict.csv", "a", encoding="cp949", newline='')
    field_name_list = ['time', 'stock']
    writer = csv.DictWriter(f, fieldnames=field_name_list)

    writer.writerow(
        {'time': t ,'stock':MaxMinScaler(test_predict)[0][1]})
    f.close()

thread_run()


urlpatterns = [
	path('', views.index),
	path('output1/', views.output1),
	path('predict1/', views.predict1),

	path('output2/', views.output2),
	path('predict2/', views.predict2),

	path('output3/', views.output3),
	path('predict3/', views.predict3),

	path('output4/', views.output4),
	path('predict4/', views.predict4),

	path('output5/', views.output5),
	path('predict5/', views.predict5),

	path('output6/', views.output6),
	path('predict6/', views.predict6),

	path('output7/', views.output7),
	path('predict7/', views.predict7),

	path('output8/', views.output8),
	path('predict8/', views.predict8),

	path('output9/', views.output9),
	path('predict9/', views.predict9),

	path('output10/', views.output10),
	path('predict10/', views.predict10),

]
