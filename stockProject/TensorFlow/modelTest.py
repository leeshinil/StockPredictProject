import tensorflowModeling as tf
import numpy as np
import pandas as pd










company = ["A005930","A000660","A035420","A017670","A006400","A018260","A003550","A036570","A035720","A251270"]

for j in company:

        tf.reset_default_graph()
        test = [[5395, 81800],
                [5492, 81800],
                [5442, 81800],
                [4724, 81800],
                [5647, 81800],
                [10980, 81800],
                [34828, 81800],
                [14239, 81800],
                [2718, 81800],
                [3916, 81800],
                [15752, 81900],
                [4326, 81900],
                [6139, 81800],
                [2768, 81900],
                [6769, 81800],
                [14784, 81900],
                [17451, 81900],
                [7942, 81800],
                [2267, 81700],
                [2496, 81700],
                [2383, 81800],
                [28982, 81700],
                [3978, 81800],
                [7447, 81800],
                [4629, 81700],
                [7665, 81700],
                [7220, 81700],
                [6383, 81800],
                [25071, 81800],
                [6459, 81800]]
        test = np.asarray(test, dtype=np.float64)

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
        testX =MinMaxScaler(test)

        # train Parameters
        seq_length = 30                                 # sequence = 7(앞에 7개값 있을 것.)
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

        saver.restore(sess, './'+j+'-model')                         # 지정한 cehckpoint 변수값 복구

        test_predict = sess.run(Y_pred, feed_dict={X: [testX]})
        print(j , " : " , MaxMinScaler(test_predict)[0][1])


