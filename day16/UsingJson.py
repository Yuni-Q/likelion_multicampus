import json

customer = {
	'id' : 1,
	'name' : '홍길동',
	'history' :[
		{'date':'2018-01-01','item':'mac'},
		{'date':'2018-01-02','item':'apple'}
	]
}

jsonString = json.dumps(customer, indent=4)
#indent는 띄어 쓰기 간격
print (jsonString)
print (type(jsonString))

dict = json.loads(jsonString)
print (dict['name'])
for i in dict['history']:
	print (i['date'],i['item'])