require 'mechanize'
require 'pry'
require 'csv'

print '뭘 찾을까요?'
input = gets.chomp
agent = Mechanize.new
agent.user_agent_alias = 'Windows Chrome'

page = agent.get('https://www.amazon.com')

search_form = page.form

#binding.pry

search_form['field-keywords'] = input

page = search_form.submit

items = page.search('.s-result-item')

items.each do |item|
  title = item.css('h2').text
  price = item.css('.a-offscreen').text
  #stars = item.css('#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(2) > div.a-column.a-span5.a-span-last > div:nth-child(1) > span > span > a > i.a-icon.a-icon-star.a-star-4-5 > span').text

  CSV.open('./amazon.csv',"a+") do |csv|
    csv << [title, price]
  end
end
#puts page
