require 'httparty'
require 'nokogiri'
require 'uri'
class HomeController < ApplicationController
  def index
  end
  def welcome
    @user = params[:user]
    #render :layout => false
  end
  def menu
    menus = ["김밥", "짜장","20층","칼국수"]
    @menu = menus.sample
  end
  def lol
    @userName = params[:user]
    puts "bb"
    if @userName == nil
      puts "aa"
      render :index
    end
    puts "cc"
    @encoded = URI.encode(@userName)
    respnse = HTTParty.get("http://www.op.gg/summoner/userName="+@encoded)
    text = Nokogiri::HTML(respnse.body)

    @win = text.css("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
    @lose = text.css("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses").text
    @tier = text.css("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank").text
  end
end
