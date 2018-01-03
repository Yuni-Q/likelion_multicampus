# 주식 정보 가져오기
# pip install googlefinane.client
from googlefinance.client import get_price_data

param = {
	'q': "GOOGL", # Stock Symbol
	'i': "86400", # 하루 단위 # Interval size(second)
	'x': "NASD", # Stock exchang Symbol
	'p': "1Y" # 1년 # Period
}
result = get_price_data(param)
print (result)