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

#  강제로 에러를 발생 시키는 경우
class Bird:
    def fly(self):
        raise NotImlemetedError
        
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

# 에러 만들기
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
