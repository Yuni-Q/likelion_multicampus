def sum(a,b):
    return a+b
def safe_sum(a,b):
    if type(a) != type(b):
        print ("더할수 없음")
        return
    else:
        result = sum(a,b)
        return result
#커맨드라인에서 실행되는 부분
if __name__ == "__main__":
	print ("ss")