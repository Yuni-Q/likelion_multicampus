require 'httparty'
require 'nokogiri'

# url = 'http://finance.naver.com/sise/'
# response = HTTParty.get(url)
# text = Nokogiri::HTML(response.body)

# kospi = text.css('#KOSPI_now')
# kosdaq = text.css('#KOSDAQ_now')
# kospi200 = text.css('#KPI200_now')
# puts "코스피는 #{kospi.text} 코스닥은 #{kosdaq.text} 코스피200은 #{kospi200.text}"

url = ("http://movie.naver.com/movie/sdb/rank/rmovie.nhn")
response = HTTParty.get(url)
doc = Nokogiri::HTML(response.body)
        
movies = []
            
# puts doc
for i in (2..11)
    #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
   	cssText = "#old_content > table > tbody > tr:nth-child(" + i.to_s + ") > td.title > div > a"
   	movie = (i-1).to_s + "위 " + doc.css(cssText).text
   	movies << movie
end

print movies
