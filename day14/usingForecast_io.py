# 날씨 가져오기 forcastio
# pip install python-forecastio
# http://github.com/ZeevG/python-forecast.io
import forecastio

api_key = "70c5061507bb119f955e97b144902649"
lat = 37.501354
lng = 127.038763

forecast = forecastio.load_forecast(api_key,lat,lng)
byHour = forecast.hourly()

print (byHour.summary)
print (byHour.icon)

for hourlyData in byHour.data:
	print (str(hourlyData.time) + "=" + str(hourlyData.temperature))