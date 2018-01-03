import tensorflow as tf
import numpy as np

x_data = [1,2,3,4,5,6]
y_data = [3,6,9,12,15,18]

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="weight")

hypothesis = x_data * W + b
cost = tf.reduce_mean(tf.square(hypothesis-y_data))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variavles_initializer())

for step in range(2000):
	sess.run(train)
	if step % 20 == 0 :
		print (step, )