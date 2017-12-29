#알고리즘 연습
#1. factorial 함수

#1 노가다
def factorial(n):
   total=1
   for i in range(1,n+1):
      total = i*total
      i =i+1
   return total

print (factorial(10))

#2내장 함수 호출
import math
print(math.factorial(10))

#3 재귀함수 이용
def fac_recur(n):
   if n <= 1: return 1
   temp = n * fac_recur(n - 1)
   return temp
print(fac_recur(10))


#계단 알고리즘
#n개의 계단을 오른다. 한번에 1,2,3개씩 오름가능.
#ex.
#입력: 3 출력:4 (1,1,1)(1,2)(2,1)(3)
#재귀 사용

def countWay(n):
   if n<0 : 
      return 0
   elif n==0:
      return 1
   else:
      return countWay(n-1)+countWay(n-2)+countWay(n-3) 

print (countWay(4))

#주어진 수중에 소수의 갯수는?
# 입력: 1000 -> 1000이하의 수 중에 소수가 몇개인지 출력 /168
#에라토스테네스의 채
#실행시간이 좋음
def prim_num(n):
   if n<2:
      return []
   s = [0,0]+[1]*(n-1)   #n개의 요소를 갖는 배열 초기화
   print(s)
   for i in range(2,int(n**.5)+1): #루트 n이하의 요소로 나누기
      if s[i]:
         s[i*2::i] = [0]*((n-i)//i)      #i의 배수 지우기
   l = [i for i, v in enumerate(s) if v]    
   return l,len(l)

l,c = prim_num(1000)
print(l)
print(c)