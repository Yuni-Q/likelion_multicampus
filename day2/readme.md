# 멀티캠퍼스 수업(ctrl+1)

- 첫번 째 입니다.(-)
  - 하위 항목 입니다 (tab)
    1. 첫번째 입니다
    2. 두번째 입니다.

```ruby
#(```ruby)
puts "hihi"
```

> 인용 구문 (>)

코스피 정보 가져오기 코드

```ruby
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

```

- 노코기리 사용
- httparty 사용



# 파일 만들기 실습

```ruby
# files 디렉토리로 옮겨
Dir.chdir("files") 

# 30개의 파일을 만듭니다.
# 1.txt ~ 30.txt
# 1.txt => 1번째 내용
# 30.txt => 30번쨰 내용
# ruby file new

(1..30).each do |number| 

	File.open("#{number}.txt", "a") {|f| f.write("#{number}번째 내용") }

end

# r- 읽기 전용. 파일이 있어야합니다.
# w - 쓰기 위해 빈 파일을 만듭니다.
# a - 파일에 추가합니다. 파일이 없으면 파일이 만들어집니다.
# r+- 읽기 및 쓰기 업데이트 파일을 엽니 다. 파일이 있어야합니다.
# w+ - 읽기와 쓰기 모두를위한 빈 파일을 만듭니다.
# a+- 읽기 및 추가를 위해 파일을 엽니 다. 파일이 없으면 작성됩니다.

# 30.times do |n|
# 	n = n+1
# 	File.open(n.to_s+".txt", "w") do |file| file.write(n.to_s+"번째 내용입니다.")
# 	end
# end
```

> 

