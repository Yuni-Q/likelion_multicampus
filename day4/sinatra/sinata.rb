require 'sinatra'

get '/' do
	"Hack your life"
end

get '/yun' do
	"hi yun"
end

get '/welcome/:name' do
	name = params['name']
	"#{name}님 반갑습니다."
end

get '/cube/:num' do

	number = params[:num]

	if number.is_a?(String)
		number = number.to_i
	end

	num3 = number ** 3

	"#{params['num']}의 세제곱은 #{num3}"
end