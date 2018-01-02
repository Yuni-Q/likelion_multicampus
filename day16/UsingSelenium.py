# pip install selenium
# https://sites.google.com/a/ chromdriver/downloads

# 다운 받아서 python과 같은 경로에 위치
from selenium import webdriver

browser = webdriver.Chrome('/Users/yunheelee/Documents/likelion_multicampus/day16/chromedriver')

browser.get("https://python.org")

# find_elements_by_id,name,class_name
menus = browser.find_elements_by_css_selector('#top ul.menu li')
pypi = None
for m in menus:
	if m.text == "PyPI":
		pypi = m

pypi.click()
