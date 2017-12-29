#numpy 사용법
import numpy as np

list1 = [1,2,3,4]
a = np.array(list1)
print (a.shape)

b = np.array(([1,2,3],[4,5,6]))
print (b.shape)
print (b[0][0])

# numpy로 배열 만들기
c = np.zeros((2,2,))
print (c)
d = np.ones((3,4))
print (d)
e = np.full((2,6),8)
print (e)
f = np.eye(3)
print (f)
g =np.array(range(20)).reshape((4,5))
print (g)

# numpy에서 indexing과 슬라이싱
lst = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
lst_n = np.array(lst)
a = lst_n[0:2,0:2]
print (a)
a = lst_n[1:,1:]
print (a)

lst = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
a = np.array(lst)
s = a[0,2]
s1 = a[1,2]
print (s)
print (s1)

# boolean indexing
# 1번 사용법
boolean = np.array([
	[False,True,False],
	[True,False,True],
	[False,True,False]
])

k = a[boolean]
print (k)

# 2번 사용법
llst = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
a = np.array(lst)
boolean2 = (a % 2 == 0)
print (boolean)
print (a[boolean2])

# numpy 연산
a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
d = a - b
e = np.multiply(a,b)
f = np.divide(a,b)
print (c) # 요소끼리 더해서 1차원 배열로 준다
print (d)
print (e)
print (f)

# 행렬, 벡터 연산
lst1 = [
	[1,2],
	[3,4]
]
lst2 = [
	[5,6],
	[7,8]
]

a = np.array(lst1)
b = np.array(lst2)
c = np.dot(a,b)
print (c)

a = np.array([
	[1,2],
	[3,4]
])
print (np.sum(a))
print (np.prod(a))
print (np.sum(a,axis=0))
print (np.sum(a,axis=1))
