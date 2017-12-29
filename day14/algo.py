# 알고리즘 연습 (http://www.codewars.com)

# webbrowser 포팅
# import webbrowser

# target = ['수지','아이유','양세형','정준하']
# url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
# wiki_url = "https://en.wikipedia.org/wiki/"

# for i in target:
# 	target_url = wiki_url + i
# 	webbrowser.open(target_url)

# forecastio + geocoder 연습

# import forecastio
# from geopy.geocoders import Nominatim

# tartget = input("어디가 궁금하세요?")
# geolocator = Nominatim()
# location = geolocator.geocode(tartget)

# api_key = "c3c46f2ceb471e5d5bf6cd29b5708bfe"
# lat = location.latitude
# lng = location.longitude

# forecast = forecastio.load_forecast(api_key,lat,lng)
# byHour = forecast.hourly()

# print (str(location)+"의 날씨는 "+byHour.summary)
# print (byHour.icon)

# for hourlyData in byHour.data:
# 	print (str(hourlyData.time)+"="+str(hourlyData.temperature))


# geocoding 포팅
# pip install geopy
# https://pypi.python.org/pypi/geopy
# from geopy.geocoders import Nominatim

# tartget = input("어디가 궁금하세요?")
# geolocator = Nominatim()
# location = geolocator.geocode(tartget)
# print ("주소 : " + str(location))
# print ("위도 : " + str(location.latitude))
# print ("경도 : " + str(location.longitude))

# [알고리즘 연습]
# 1. factorial algorithm
# def factorial(4) => 4*3*2*1 반환하는 함수
# def factorial(6) => 6*5*4*3*2*1 반환하는 함수

# 1 번 방법
# import math
# print (math.factorial(10))

# # 2 번 방법
# def factorial_yame(n):
# 	l = range(1,n+1)
# 	result = 1
# 	for i in l:
# 		result = result* i
# 	return result
# print (factorial_yame(10))

# # 3 번 방법 (재귀 이용)
# def factorial(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * factorial(n-1)
# print (factorial(10))

# [알고리즘 연습]
# 2. n개의 계단을 오른다. 한번에 1개,2개,3개씩 오를수 있다.
# 계단을 오르는 경우의 수가 몇가지 있는지 구하는 함수를 구하라
# ex. 계단의 갯수가 
# 입력: 3, 출력: 4 _ (1,1,1),(1,2),(2,1)(3)
# 입력: 4, 출력: 7 _ (1,1,1,1)(1,1,2)(1,2,1)(2,1,1)(2,2)(3,1)(1,3)
# 재귀 사용
# def countWay(n):
# 	if n<0:
# 		return 0
# 	elif n == 0:
# 		return 1
# 	else:
# 		return countWay(n-1) + countWay(n-2)+countWay(n-3)
# print (countWay(5))

# [알고리즘 연습]
# 3. 주어진 수 중에 소수가 몇개 인지 출력하는 프로그램
# 입력 : 1000 -> 1000이하의 수 중에 소수가 몇개인지 출력/168
# 키워드 : 에라토스테네스의 체
# def countPrime(n):
# 	if n < 2 : 
# 		return []
# 	s = [0,0] + [1] * (n-1) # 1000개의 요소를 갖는 배열 초기화

# 	for i in range(2,int(n**.5)+1): # 루트 n이하의 요소로 나누
# 		if s[i]:
# 			s[i*2::i] = [0] * ((n-i)//i) # i의 배수 지우기
# 	l = [i for i, v in enumerate(s) if v] # 리스트만들기
# 	return l, len(l)

# l,c = countPrime(1000)
# print (l)
# print (c)