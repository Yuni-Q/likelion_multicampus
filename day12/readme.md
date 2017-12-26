# day12

- 오늘부터 파이썬 !!
- 파이썬 설치
  ```bash
  brew install python3
  sudo easy_install pip
  pip3 install —upgrade pip
  ```
- anaconda 다운
- jupyter 설치
  ```bash
  Pip3 install jupyter
  jupyter notebook
  ```
- anaconda로 tensor flow 설치
  ```Bash
  create conda -n tensorflow python=3.6
  source activate tensorflow
  pip install tensorflow
  {
  python
  import tensorflow as tr
  tf.__version__
  }
  ```
- Python 문법
  ```python
  print ("hello world") #()가 필수 !!
  head = "Aa"
  tail = "Bb"
  print (head+tail) # AaBb
  print("="*30) # ==============================

  #슬라이싱, 인덱스
  a = "my name is yunhee"
  print (a[3]) # n
  print (a[-3]) # h 뒤에서 부터 !!
  print (a[0:4]) # my n 0부터 4미만 !!
  print (a[11:]) # yunhee 11부터 끝까지
  print (a[:]) # my name is yunhee 모두 출력 !!
  s = "Apple"
  num = 100
  print ("블라 %s 블라" %s) # 블라 Apple 블라 # s는 string
  print ("블라 %i 블라" %num) #블라 100 블라 # i는 integer
  print ("블라 %s %i 블라" %(s,num)) # 블라 Apple 100 블라
  print ("%d%%" %95) # 95% # %d는 숫자 %%는 %를 출력한다 !!
  print ("%10s" %"hi") #         hi # 공백 만들기
  print ("%-10s hi" % "hello") # hello      hi 
  print ("%0.4f" %3.1458124156) # 3.1458
  print ("%10.4f" %3.1415603503) #     3.1416
  s = "hello"
  s.count("l") # 2 # l이 2개 있다
  s = "hello"
  s.index("e") # 1 # 1번 자리에 e가 있다

  #빈출
  a ="."
  a.join("abcde") # 'a.b.c.d.e'
  a = "HI"
  a.lower() # 'hi'
  a = '  hi  '
  print (a.lstrip().rstrip()) # hi
  print (a.strip()) # hi
  a = 'apple grape'
  print (a.replace("apple","melon")) # melon grape
  print (a.split()) # ['apple', 'grape']
  b ="2016:12:31:Rainy"
  print (b.split(":")) # '2016', '12', '31', 'Rainy']
  print (len(a)*len(b)) # 176 #len 길이 구하는거

  type("pithon") #str
  3**4 # 81
  7%3 # 1
  7//3 # 2 #몫만
  7/3 # 2.3333333
  print ("블라블라",47*8,"블라") # 블라블라 376 블라
  a = [1,2,3]
  print (a) # [1, 2, 3]
  print (a[1]) # 2
  print (a[-1]) # 3

  a = [1,2,[3,4]]
  print (a[-1]) # [3, 4]
  print (a[-1][-1]) # 4
        
  a = [1,2,3,4,5,8]
  if 4 in a:
  	print ("응 있어") # 응 있어
            
  a.append(77)
  a.sort()
  a.reverse()
  a.index(8)
  a.remove(3)
  a.pop
  a.count(77)
  a.extend([999,9999])

  # Array 관련 함수들
  [1,2,3,4]
  # tuple 관련 함수들
  c = (1,2,3,4) # 튜플은 수정이 안 된다 !!
  # 더하기, 곱하기는 가능
  s = "hello"
  t = tuple(s)
  print (t)	# ('h', 'e', 'l', 'l', 'o')
  dic = {'key1':'value1','key2':'value2','key3':'value3'}
  dic['key4'] = 'value' # 추가
  del dic['key2'] #삭제
  print (dic['key1'])
  dic.key() # 키 값 가져오기
  dic.value # 값 가져오기
  dic.item()
  dic.clear() # 딕셔너리 초기화

  dic.get('key1') # 없는 값 에러 안 남
  dic.get('ket1', '없습니다.') # 2번째 인자는 없을 때 출력 할 값
  dic['key1'] # 없는 값 에러 남 !!

  # Set 집합 - 중복 X 손서 X (인덱싱, 슬라이싱 X)
  list = [1,1,1,5,9,6,3]
  a = set(list)

  list2 = [1,6,8,5,19,6,3]
  b = set(list2)

  print (a&b) # 교집합
  print (a.intersection(b))
  print (len(a&b))

  print (a|b) # 합집합
  print (a.union(b))
  print (len(a|b))

  print (a-b) # 차집합
  print (b-a)
  print (a.difference(b))

  a.add(999)
  a.update([66,77,88]) # set update
  a.remove(77) #set 삭제
  print (a)

  if []:
      print ("A")
  else:
      print ("B") # B # 빈 리스트는 false
      
  a = [1,2,3,4]
  while a:
      print (a.pop()) # 4 3 2 1
      
  a = 3
  b = 3
  print (a is b)

  a,b = (3,3)
  c,d = [4,4]
  e=f=5
  print (a,b,c,d,e,f)

  a = [1,2,3]
  b = a # 같은 배열 쳐다보고 있음
  c = a[:] # 다른 배열 쳐다보고 있음
  a[1] = 5
  print (b) # [1,5,3]
  print (c) # [1,2,3]

  if 1: # 1은 true 0은 false
      print ("a")
  else:
      print ("b")
      
  # tab과 클론(:)이 중요하다

  if 1 in [1,2,3,4]:
      pass # 아무것도 안함
  else:
      print ("B")
      
  # 입력 받기
  a = input("이름을 입력해 주세요.")
  print (a)

  for i in range(10):
      print (i)
      # 0 1 2 3 4 5 6 7 8 9
      
  for i in range(2,10):
      for j in range (1,10):
          print ("%i * %i = %i" %(i,j,i*j), end=" ")
      print ("")
  # 2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 2 * 4 = 8 2 * 5 = 10 2 * 6 = 12 2 * 7 = 14 2 * 8 = 16 2 * 9 = 18 
  # 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 3 * 4 = 12 3 * 5 = 15 3 * 6 = 18 3 * 7 = 21 3 * 8 = 24 3 * 9 = 27 
  # 4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 4 * 5 = 20 4 * 6 = 24 4 * 7 = 28 4 * 8 = 32 4 * 9 = 36 
  # 5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 5 * 6 = 30 5 * 7 = 35 5 * 8 = 40 5 * 9 = 45 
  # 6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 6 * 7 = 42 6 * 8 = 48 6 * 9 = 54 
  # 7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 7 * 8 = 56 7 * 9 = 63 
  # 8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 8 * 9 = 72 
  # 9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81 

  a = [1,2,3]
  result = []
  # result = [num * 3 for num in a]
  result = [num * 3 for num in a if num % 2 == 0]
  print (result)
  # [6]
  ```

