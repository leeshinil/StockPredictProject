from django.shortcuts import render

from django.http import HttpResponse

import json
import tensorflow as tf
import csv
import pandas as pd
import time
import datetime
import numpy as np
import threading

def index(request):
    return render(request, 'serverTest/index1.html')


#과거 캔들 차트 그리기
def output1(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A005930_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict1(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A005930_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A005930_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output2(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A000660_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict2(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A000660_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A000660_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output3(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A035420_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict3(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A035420_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A035420_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output4(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A017670_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict4(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A017670_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A017670_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output5(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A006400_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict5(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A006400_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A006400_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output6(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A018260_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict6(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A018260_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A018260_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output7(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A003550_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict7(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A003550_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A003550_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output8(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A036570_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict8(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A036570_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A036570_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output9(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A035720_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict9(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A035720_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A035720_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#과거 캔들 차트 그리기
def output10(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A251270_candle.csv", "r")
    for line in file:
         customer_list.append(line.strip('\n'))
    del customer_list[0]
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#예측값 차트 그리기
def predict10(request):
    test1_counter = 0
    test2_counter = 0
    now = []
    pre = []
    customer_list = []
    delete = 0
    file = open("A251270_now.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1
    if (test1_counter > 20 ):
        delete = test1_counter / 10
        delete = delete - 1
        delete = delete * 10

    del now[:int(delete)]
    file2 = open("A251270_predict.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1
    if (test2_counter > 20 ):
        delete = test2_counter / 10
        delete = delete - 1
        delete = delete * 10

    del pre[:int(delete)]
    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")
