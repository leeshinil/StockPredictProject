# 이전 시장 변동가격 보고 내일의 값은 얼마일까? 예측하기
import tensorflow as tf
import numpy as np

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

company = ["A005930","A000660","A035420","A017670","A006400","A018260","A003550","A036570","A035720","A251270"]
for j in company:
    tf.reset_default_graph()
    tf.set_random_seed(777)  # reproducibility재현성


    def MinMaxScaler(data):
        numerator = data - np.min(data, 0)
        denominator = np.max(data, 0) - np.min(data, 0)
        # noise term prevents the zero division
        return numerator / (denominator + 1e-7)


    # train Parameters
    seq_length = 30                                 # sequence = 30
    data_dim = 2                                    # input data는 한번에 들어감
    hidden_dim = 10                                 # 10개 hidden 있을 것.
    output_dim = 1                                  # output = 1
    learning_rate = 0.01
    iterations = 500

    # Open(오픈할때 얼마), High(가장 높을때), Low(가장 낮을때), Volume,(이날 얼마나 팔렸어) Close
    xy = np.loadtxt('C:/Users/lexsh/Desktop/server/'+ j +'_pastStock.csv', delimiter=',', skiprows=1)

    # print(xy)
    # # 데이터 전처리
    # # xy = xy[::-1] # 제일앞이 뒤로, 제일뒤가 앞으로 순서를 뒤집는다.
    xy = MinMaxScaler(xy)
    x = xy[:,[2, 3]]
    y = xy[:, [-1]] # 마지막 열이 정답(주식 종가)이다.

    # build a dataset
    dataX = []
    dataY = []

    # 마지막 넣은것까지 하나씩 윈도우 옮겨가면서 돌게 됨.
    for i in range(0, len(y) - seq_length):
        _x = x[i:i + seq_length]
        _y = y[i + seq_length]                              # Next close price
        # print(_x, "->", _y)                                 # 30개 값으로 y값 예측할것.
        dataX.append(_x)                                    # 각각 array list에 쌓아줌.
        dataY.append(_y)

    # train/test split
    train_size = int(len(dataY) * 0.7)                      # 70퍼 train,
    test_size = len(dataY) - train_size                     # 나머지 test로.
    trainX, testX = np.array(dataX[0:train_size]), np.array(# 가져오게 됨.
        dataX[train_size:len(dataX)])
    trainY, testY = np.array(dataY[0:train_size]), np.array(
        dataY[train_size:len(dataY)])

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

    # RMSE 평균제곱근편차
    targets = tf.placeholder(tf.float32, [None, 1])
    predictions = tf.placeholder(tf.float32, [None, 1])
    rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        # Training step 500번 학습 시킴
        for i in range(500):
            _, step_loss = sess.run([train, loss], feed_dict={X: trainX, Y: trainY})

        saver = tf.train.Saver() #학습모델링
        saver.save(sess, "C:/Users/lexsh/Desktop/server/" + j + "-model") #학습 모델링 구축

    # Test step
    # test_predict = sess.run(Y_pred, feed_dict={X: testX})
    # rmse_val = sess.run(rmse, feed_dict={ targets: testY, predictions: test_predict})
    # print("RMSE: {}".format(rmse_val))
    #
    # print(testY, '= ' , test_predict)
    #
    # # Plot predictions
    # plt.plot(testY)                                     # 원래의 데이터와
    # plt.plot(test_predict)                              # 예상한 데이터를 찍어본다.
    # plt.xlabel("Time Period")
    # plt.ylabel("Stock Price")
    # plt.show()