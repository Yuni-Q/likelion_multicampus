import tensorflow as tf
import numpy as np

### Softmax Classification 실습 ##
### 데이터 : 공유폴더내/iris.csv
xy = np.loadtxt('iris.csv',delimiter=',',dtype=np.float32)
x_data = xy[:,0:-1]
y_data = xy[:,[-1]]

### Softmax Classification ####
# xy = np.loadtxt('data-04-zoo.csv', delimiter=",", dtype=np.float32)
# x_data = xy[:,0:-1]
# y_data = xy[:,[-1]]

# print (x_data, y_data)

X = tf.placeholder(tf.float32, [None,4])
Y = tf.placeholder(tf.int32, [None,1])

# One Hot Encoding
Y_one_hot = tf.one_hot(Y,4)
Y_one_hot = tf.reshape(Y_one_hot,[-1,4])

W = tf.Variable(tf.random_normal([4,4]), name='weight')
b = tf.Variable(tf.random_normal([4]), name='bias')

logits = tf.matmul(X,W)+b
hypothesis = tf.nn.softmax(logits)

# Cross Entropy
cost_i = tf.nn.softmax_cross_entropy_with_logits(
		logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# accuracy 계산
prediction = tf.argmax(hypothesis,1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())

	for step in range(2000):
		sess.run(optimizer, feed_dict={X:x_data, Y:y_data})
		if step % 100:
			loss, acc = sess.run([cost, accuracy], 
							feed_dict={X:x_data, Y:y_data})
			print ("Step=",step,"Loss=",loss,"Acc=",acc,"\n")

	pred = sess.run(prediction, 
							feed_dict={X:x_data})

	# 실제 값과 비교
	for p, y in zip(pred, y_data.flatten()):
		print (p,y)
