require 'sinatra'
require 'csv'


get '/' do
	erb :index

end

get '/vote' do
	@user = params[:user]
	@vote = params[:vote]
	
	CSV.open('vote.csv',"a+") do |v|
		v << [@user, @vote]
	end

	erb :vote
end

get '/result' do
	@list = Array.new

	CSV.foreach("vote.csv") do |row|
		@list << row
	end
	erb :result
end