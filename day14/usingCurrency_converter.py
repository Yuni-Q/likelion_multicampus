# 환율 변환
# pip install --user currencyconverter
from currency_converter import CurrencyConverter
from datetime import date
c =  CurrencyConverter()
print (c.convert(100,'EUR','USD'))
print (c.convert(100,'EUR','USD',date=date(2016,6,24)))

print (c.convert(100,'EUR')) # 디폴트 값 알아보기 # 기본값은 유로
print (c.convert(100,'USD'))