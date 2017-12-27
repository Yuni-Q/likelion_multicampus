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
