require 'sinatra'
require 'httparty'
require 'nokogiri'
require 'uri'

#require 'csv'
#require 'data'
get '/' do
	erb :index
end

get '/search' do
	@id = params[:userName]
	@win = 0 
	@lose = 0

	@encoded = URI.encode(@id)
	response = HTTParty.get("http://www.op.gg/summoner/userName=" + @encoded)

	html = Nokogiri::HTML(response.body)
	@win = html.css("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
	@lose = html.css("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses")
	@tier = html.css("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span")

	

	File.open('log.txt',"a+") do |f|
		f.write("#{@id}, #{@tier.text}, #{@win.text}, #{@lose.text} \n")
	end

	CSV.open('log.csv', "a+") do |c|
		c << [@id, @tier.text, @win.text, @lose.text, Time.now.to_s]
	end

	erb :search

end 

before do

end