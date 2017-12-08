require 'launchy'

key = ["수지", "아이유", "워너원", "BTS"]
url = "https://search.naver.com/search.naver?query="

key.each do |member|
	Launchy.open(url+member)
end