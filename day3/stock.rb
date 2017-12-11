require "stock_quote"
require 'eu_central_bank'

# 환율 구하기 
from = 'USD'
to = "KRW"

bank = EuCentralBank.new
bank.update_rates 

result = bank.exchange(100, from, to)

# companies를 돌면서 요소별로
DATA.each do |company|
	company.chomp!
	stock = StockQuote::Stock.quote(company)
	stock.l.gsub! ',',''
	puts stock.l
	currency = stock.l.to_f * result
	puts "#{stock.name}의 가격은 $ #{currency}원"
end

__END__
googl
aapl
tsla
msft
fb
