require 'forecast_io'

ForecastIO.configure do |configuration|
  configuration.api_key = '70c5061507bb119f955e97b144902649'
end

forecast = ForecastIO.forecast(37.8267, -122.423)

puts forecast