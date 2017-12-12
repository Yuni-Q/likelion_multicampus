require 'sinatra'

get '/' do
	"<h1>점심 빨리 먹고 싶다</h1>"
end

get '/intro' do 
	send_file "intro.html"
end

get '/outro' do
	@name = 'yun' 
	erb :outro
end

get '/lunch' do
	@menus = ['kimchi', '20','GS','pizz']
	@eats = ['드세요','먹어라','먹던가']
	@menu = @menus.sample + @eats.sample
	erb :lunch
end