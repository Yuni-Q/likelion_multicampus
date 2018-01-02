# Random
from random import *

# i = random()
# print (i)
# 0~1 사이의 랜덤값

# i = randint(1,100)
# print (i)
#1~100 사이의 랜덤 int 값

# i = uniform(1.0,36.5)
# print (i)
# # flot 값

# o = randrange(0,100,2)
# print (o)
# # 짝수

# 난수 맞추기 게임
# 1,100 사이의 정수가 랜덤으로 생겨요
# while 돌면서 맞추면 종료, 못 맞추면 다시 맞추기

randNum = randint(1,100)
while True:
	ans = input("맞춰봐!","종료하려면 Q")

	if (ans == "Q")
		break
	if int(ans)==randNum:
		print ("축하합니다!! 정답입니다")
	elif int(ans)<randNum:
		print ("값이 너무 작아요 !!")
	else:
		print ("값이 너무 커요 !!")
