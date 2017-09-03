# -*- coding: utf-8 -*-
from pandas import DataFrame, Series
import sys, os
import numpy as np
import pandas as pd
import tensorflow as tf

reload(sys)
sys.setdefaultencoding('utf-8')

xy = np.loadtxt('/home/park/Desktop/lol_project/rankData.txt', unpack=True)

x_data = xy[0:-1]
y_data = xy[-1]


test = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [2], [0], [0], [0], [3], [0], [3], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [2], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [3], [0], [0],
 [0], [0], [0], [2], [0], [2], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [3], [0], [0], [3], [0], [2], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0]]

test2 = [[0], [2], [0], [0], [0], [0], [0], [0], [3], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [2], [0], [0], [0], [0], [3], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [3], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [2], [0], [0], [0], [2], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [2], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [3], [0], [0], [0],
 [0], [3], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0]]

test3 = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [2], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [3], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [2], [0], [0], [0], [0], [0], [2], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [3], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [3], [0], [0], [0], [0], [2], [0], [0], [0],
 [0], [0], [0], [3], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [2], [0], [0], [3]]


# win
test4 = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [2], [0], [0], [0], [0], [0],
 [2], [0], [0], [0], [0], [0], [3], [0], [0], [0],
 [0], [0], [0], [2], [0], [3], [0], [2], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [3], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [2], [0], [0], [3], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [3], [0], [0],
 [0], [0], [0], [0]]


#loss
test5 = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [3], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [2], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [3], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [3], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [3], [0],
 [0], [0], [2], [0], [0], [0], [0], [0], [0], [3],
 [0], [0], [0], [0], [0], [2], [0], [0], [0], [0],
 [0], [0], [2], [0], [2], [0], [0], [0], [0], [0],
 [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
 [0], [0], [0], [0]]


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)


W = tf.Variable(tf.random_uniform([1, len(x_data)], -1.0, 1.0))

h = tf.matmul(W, X)
hypothesis = tf.div(1., 1. + tf.exp(-h))

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis)) 

alpha = tf.Variable(0.05)
optimizer = tf.train.GradientDescentOptimizer(alpha)
train = optimizer.minimize(cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in xrange(50000):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 1000 == 0:
        print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}))

print(sess.run(hypothesis, feed_dict={X:test}) > 0.5)
print(sess.run(hypothesis, feed_dict={X:test2}) > 0.5)
print(sess.run(hypothesis, feed_dict={X:test3}) > 0.5)
print(sess.run(hypothesis, feed_dict={X:test4}) > 0.5)
print(sess.run(hypothesis, feed_dict={X:test5}) > 0.5)