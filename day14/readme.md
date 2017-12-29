# Day 14

- join

  ```python
  def isAnagram2(s1,s2):
      a =''.join(sorted(s1.lower())).strip()
      b =''.join(sorted(s2.lower())).strip()
      if a == b :
          return True
      else:
          return False
      
  print (isAnagram2("ABC","BCA"))
  print (isAnagram2("ABC","CDD"))
  ```

  ```python
  food = ["123","apple","dlrjt","wjrjt"]
  print (''.join(food))
  print ('/'.join(food))
  print (','.join(food))
  print ('\n'.join(food))
  ```

- 피보나치 수열

  ```python
  def Fibonacci(n):
      a = 1
      b = 1
      c = 0
      d = 3
      if n < 3:
          return 1
      for i in range(3,n+1):
          c = a + b
          a = b
          b = c
      return c

  print (Fibonacci(10))
  ##############################
  def Fibonacci2(n):
      result = [0,1]
      
      for i in range(2,n+1):
          result.append(result[i-1]+result[i-2])
      return result[-1]

  print (Fibonacci2(10))
  ```

- numpy

  ```python
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
  ```

- Bumpy 연산

  ```python
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
  print (np.sum(a)) # 다 더하기
  print (np.prod(a)) # 다 곱하기
  print (np.sum(a,axis=0)) # 기준
  print (np.sum(a,axis=1)) # 기준. # 들어갈수록 커짐
  ```

- currencyconverter

  ```bash
  pip install --user currencyconverter
  ```

  ```python
  # 환율 변환
  # pip install --user currencyconverter
  from currency_converter import CurrencyConverter
  from datetime import date
  c =  CurrencyConverter()
  print (c.convert(100,'EUR','USD'))
  print (c.convert(100,'EUR','USD',date=date(2016,6,24)))

  print (c.convert(100,'EUR')) # 디폴트 값 알아보기 # 기본값은 유로
  print (c.convert(100,'USD'))
  ```

- forcastio

  ```python
  # 날씨 가져오기 forcastio
  # pip install python-forecastio
  # http://github.com/ZeevG/python-forecast.io
  import forecastio

  api_key = "70c5061507bb119f955e97b144902649"
  lat = 37.501354
  lng = 127.038763

  forecast = forecastio.load_forecast(api_key,lat,lng)
  byHour = forecast.hourly()

  print (byHour.summary)
  print (byHour.icon)

  for hourlyData in byHour.data:
  	print (str(hourlyData.time) + "=" + str(hourlyData.temperature))
  ```

  ​