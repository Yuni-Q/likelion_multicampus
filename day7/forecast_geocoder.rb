require 'forecast_io'
require 'geocoder'
require 'pry'

ForecastIO.configure do |configuration|
  configuration.api_key = '70c5061507bb119f955e97b144902649'
end

def f_to_c(f)
  # (화씨 - 32) * 5/9
  c = ((f-32) * 5/9).round(1)
  return c
end

print '어디가 궁금하세요? : '
location = gets.chomp!

loCord = Geocoder.coordinates(location)

#binding.pry

forecast = ForecastIO.forecast(loCord[0],loCord[1])

f = forecast.currently
puts f.summary
puts f_to_c f.apparentTemperature
