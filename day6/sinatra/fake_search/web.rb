require 'sinatra'

# '/' => index
# index.erb
# => 뭐든 검색합니다.

get	'/' do
	erb :index
end