# Python Crawling 
#-*-coding:utf-8
import urllib.request
from bs4 import BeautifulSoup 

req = urllib.request.Request("http://finance.naver.com/sise/")
data = urllib.request.urlopen(req).read()
bs = BeautifulSoup(data, 'html.parser')

target = ['KOSPI_now','KOSDAQ_now','KPI200_now']
for i in target:
    print (i+" = "+bs.find(id=i).get_text())