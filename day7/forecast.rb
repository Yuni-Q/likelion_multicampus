require 'forecast_io'
require 'pry'
require 'awesome_print'


def f_to_c(f)
  # (화씨 - 32) * 5/9
  c = ((f-32) * 5/9).round(1)
  return c
end

ForecastIO.configure do |configuration|
  configuration.api_key = '70c5061507bb119f955e97b144902649'
end

#ap forecast

#binding.pry

forecast = ForecastIO.forecast(37.8267, -122.423)

c = forecast.currently

puts "현재 날씨는 #{c.summary}이고 섭씨 #{f_to_c c.apparentTemperature}"
