# day 13

- python 문법

  ```python
  # 1. 입력 출력 o
  def sum(a, b):
      result = a+b
      return result
  # 2. 입력 출력 x
  def say():
      print ("hi")
  # 3. 입력 o 출력 x
  def say_a(a):
      print (a)
  # 3. 입력 x 출력 o
  def say_b():
      return 100

  print (sum(1,2))
  say()
  say_a("hihihihihihihihihi")
  c = say_b()
  print (c)

  def say_list(list):
      sum = 0
      for num in list:
          sum = num + sum
      avg = sum / len(list)
      return avg #리스트 내의 element들의 평균을 반환
  list = [1,2,3]
  print (say_list(list))

  def sum (*args): # 들어오는 만큼 받아서 튜플로 만든다 
      sum = 0
      for i in args:
          sum += i    
      return sum
  print (sum(1,2,3,4,5))

  def sum_mul(choice, *args): # 여러가지 사용
      if choice == 'sum':
          result = 0
          for i in args:
              result = result + i
      elif choice == 'mul':
          for i in args:
              result = result * i
      return result

  print (sum_mul('sum',1,2,3,5,6,7))
  print (sum_mul('mul',1,2,3,4,5))

  def sum(a,b): # return 2개
      return a+b, a*b

  l,r = sum(1,2)
  print (l)
  print (r)
   
  def say(name): # 함수 끝내기
      if name == "ko":
      # 아무말도 안해
          return
      print (name)
      
  say("ko")
  say("ka")

  # 값을 주지 않아도 디폴트 값이 있는 함수
  def say_myself(name,old,man=True):
      print ("나의 이름은 %s 나이는 %s 입니다" %(name,old))
      if man:
          print ("남자")
      else:
          print ("여자")
          
  say_myself("yun",26)
  say_myself("hee",31,False)
  # true false 대문자로 써야 합니다.

  # 출력 값은 1이 나온다
  # 전역변수와 지역변수의 차이
  # global a로 지역 내에서도 전역 변수로 사용 할 수 있으나 좋은 방법이 아니다
  # return을 쓰는 것을 추천
  a = 1
  def bb(a):
      a = a+1
  bb(a)
  print (a)

  print ("A""B""C") # print ("A"+"B"+"C")와 같다
  print ("A", "B", "C")

  # 1차원 점이 주어 졌을 때 가장 거리가 짧은 쌍을 출력 하시오.
  def point(list):
      result = float('inf') # 최대값 #float('-inf')
      a = 0
      b = 0
      for i in list:
          for j in list:
              if i-j != 0:
                  if abs(i-j)<result: # abs는 절대값
                      result = abs(i-j)
                      a = i
                      b = j
      return a,b
  c,d = point([1,3,4,8,13,17,22])
  print (c)
  print (d)
  ```

- Txt 만들기 

  ```python
  # 쓰기
  f = open("aa.txt","w")
  for i in range(10):
      data = "%d lines \n" %i
      f.write(data)
  f.close()

  # 한줄 읽기
  f = open("aa.txt","r")
  result = f.readline()
  print (result)
  f.close()

  # 여러 줄 읽기
  f = open("aa.txt","r")
  lines = f.readlines()
  for line in lines:
      print (line)
  f.close()

  # 파일 전체 문자열 읽기
  f = open("aa.txt", "r")
  data = f.read() # 파일 전체 문자열을 읽는 메소드
  print (data)
  f.close()

  # 옵션 a
  f = open("aa.txt","a")
  for i in range(10):
      data = "%d lines \n" %(i+10)
      f.write(data)
  f.close()

  # with문을 쓰면 close() 안 써도 된다
  with open("aa.txt","a") as f:
      for i in range(10):
          data = "%d lines \n" %(i+10)
          f.write(data)
  ```

- Class

  ```python
  # Class, Module
  # 자바에서 Class : 재사용성
  # a(객체, 클래스의 인스턴스) = Class
  class Calculator:
      def __init__(self): # 초기값
          self.result = 0
      def add(self, num): # self 무조거 넣어 줘야 함 # 함수가 클래스 소속임을 알 수 있다(?)
          self.result = self.result + num
          return self.result
      
  a = Calculator()
  b = Calculator()
  print (a.add(3))
  print (a.add(4))

  print (b.add(3))
  print (b.add(5))

  class Service:
      secret = "Hello"

  Service.secret = "hi" # 이것만 바꾸면 a,b 값 둘다 바뀜
      
  a = Service()
  print (a.secret)

  b = Service()
  print (b.secret)

  #class 안에 함수와 메소드가 있고 사용법을 설명 했다
  ```

- class 상속

  ```python
  class HousePark:
      lastname = "박"
      def __init__(self,name):
          self.fullname = self.lastname + name
  #     def setname(self, name):
  #         self.fullname = self.lastname + name
      def __add__(self, other): # 규칙 지켜 줘야함
          print ("%s, %s 결혼함" %(self.fullname, other.fullname))
      def travel(self,where):
          print ("%s, %s 여행을 가다" %(self.fullname, where))
          
  pey = HousePark("호우")
  #pey.setname("호우")
  pey.travel("러시아")

  class HouseKim(HousePark):
      lastname = "김"
      #오버라이딩
      def travel(self,where,day):
          print ("%s %s 여행을 %s에 가다." %(self.fullname,where, day))
      
  pi = HouseKim("하야")
  pi.travel("미얀마",5)
  pey + pi # 위에서 __add__라는 규칙을 지켰기에 사용 가능 # 오버로딩
  ```

- Module

  ```python
  PI = 3.141592

  class Math:
  	def solv(self, r):
  		return PI * (r**2)

  def sum(a,b):
  	return a+b

  if __name__ == "__main__":
  	print(PI)
  	a = Math()
  	print (a.solv(2))
  	print (sum(PI,4.4))
  # module은 따로 만들어 import해서 사용한다
  # if __name__ == "__main__": 은 테스트용으로 많이 사용한다

  # 다른 경로에 있으면 sys.path.append("주소") 해야 한다
  # 경로 설정하기
  import sys
  sys.path.append("/Users/yunheelee/Documents/likelion_multicampus/day13/apple")
  print (sys.path)
  ```

- 에러 처리

  ```python
  try:
      4/0
  except ZeroDivsionError as e:
      print(e)

  # else, finally    
  try:
      f = open("a.txt", "r")
  except FileNoFoundError as e:
      print(e)
  else:
      print ("?")
  finally: # 무조건 실행
      f.close()

  # 2개를 한번에
  try:
  	a = [1,2]
      print (a[3])
      4/0
  except indexError as e:
      print(e)
  except ZeroDivsionError as e:
      print(e)
    
  # 한줄에 혹은 무시
  try:
  	a = [1,2]
      print (a[3])
      4/0
  except (indexError,ZeroDivsionError) as e:
      pass

  ```

- 강제 에러 발생

  ```python
  # 강제로 에러를 발생 시키는 경우
  # 협업 하는경우 # 따로 개발하라고 일부러 에러를 발생
  class Bird:
      def fly(self):
          raise NotImlemetedError
          
  class Eagle(Bird):
      pass

  eagle = Eagle()
  eagle.fly()
  ```

- 에러 만들기

  ```python
  class MyError(Exception):
      def __str__(self):
  	return "내가 만든 에러 입니다"    
  def say_nick(nick)
  	if nick == "min"
      	raise MyError()
      print (nick)
  try:
      say_nick("min")
  except MyError as e:
      print (e)
  ```

- 내장 함수

  ```python
  print (max([1,2,3,4,5,6])) # 최대값
  print (abs(-11)) # 절대값
  print (all([1,2,3,4,5])) # 모두가 참인가? # 하나라도 false이면 false
  print (any([0,0,0,0,0,0])) # 하나라도 참이면 True
  print (chr(97)) # 아스키코드가 97인 문자를 출력
  print (ord('a')) # 거꾸로 97이 나옴
  print (dir([1,2,3])) # 지원하는 메소드 들을 출력해서 알려준다
  print (divmod(7,3)) #몫과 나머지를 튜플로 준다
  for i, name in emumerate(["A","B","C","D"]):
  	print (i, name) # index와 키를 모두 출력
  print (eval('1+2')) # 연산 안 되는 스트링을 연산이 되게 한다
  print (eval("'hello'+'a'")) 

  def positive(x):
  	return x > 0

  print (list(filler(positive,[1,-3,5,-8]))) # True인 것과 뽑아서 리스트로 만든다

  print (pow(2,4)) # 2의 4승
  print (range(1,10,2)) # 1~9를 만드는데 간격이 2
  print (sorted[3,1,2]) # 정렬
  print (sorted("zero")) # 알파벳 순으로 정렬
  list(zip([1,2,3],[4,5,6])) # ([1,4],[2,5],[3,6]) # 스트링도 가능

  sum = Lambda a,b : a+b # Lambda funtion # 함수형렝귀지
  print(sum(3,4))

  myList = [Lambda a,b: a+b, Lambda a,b:a*b]
  print (myList[0](3,4)) # 7
  print (myList[1](3,4)) # 12

  def two_times(x):
  	return x*2
  list(map(two_times,[1,2,3,4,5])) # 적용 시키고 반환하고 적용 시키고 반환하고 .....
  list(map(Lambda a:a*3,[1,2,3,4,5])) # 람다 더하기
  ```

- 내장함수2

  ```python
  import webbrowser
  webbrowser.open("http://naver.com")
  webbrowser.open_new("http://naver.com")

  import random
  print (random,random())
  print (random,random(1,10))

  import calender
  print (calender.calender(2017))
  print (calender.prmonth(2017,12))


  import time

  print (time.strftime('%x',time.localtime(time.time)))
  print (time.strftime('%c',time.localtime(time.time)))
  for i in range(10):
  	print (i)
  	time.sleep(1)
  ```

  ​