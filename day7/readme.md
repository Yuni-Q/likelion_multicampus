# day 07

```bash
vagrant up
vagrant ssh
vagrant halt
```

> up => 깨우기
>
> ssh => 접속
>
> halt => 끄기규

```bash
rbenv version
```

> ruby 버전 확인 !!

```bash
rbenv global 2.4.2
```

> 글로벌하게 2.4.2 버전을 쓰겠다.

```bash
git clone http://githun.com/classhana/likelion
```

> 깃 클론 다운 받기 !!

- forecast 재시도 !!

  - 함수정의

  ```ruby
  def 함수이름
  end
  ```

  - gemfile을 쓰기 위해

  ```bash
  gem istall bundler
  bundle install
  gem list
  ```

  > 젬도 버전별로 관리 되서 버전 바꾸면 다시 gem install 해야 한다 !!

  ```bash
  irb
  exit
  ```

  > irb => 대화하자
  >
  > exit => 대화 끝내자

  ```ruby
  def f_to_c(f=0)
    # (화씨 - 32) * 5/9
    c = ((f-32) * 5/9).round(1)
    return c
  end
  ```

  > 초기값을 0으로 준다 !!!
  >
  > 에러를 뿝는 것보다 0을 초기값으로 하는 것이 나을 때 사용 할 수 있겠다 !!

  ```ruby
  require 'pry'
  require 'awesome_print'

  ap forecast

  binding.pry #디버깅

  ```

  > gem awesome_print는 출력 값을 이쁘게
  >
  > ap로 출력 하는 듯
  >
  > gem pry
  >
  > binding으로 중간에 멈춰서 값을 가지고 놀 수 있다 !!  (Ctrl+D로 끝낸다)

- scraper

  ```ruby
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
  ```

  ```bash
  pry
  ```

  > irb와 비슷하게 쓸 수 있다.

- artii

  ```ruby
  require 'artii'

  a = Artii::Base.new({font: 'acrobatic'})
  puts a.asciify('hana)
  ```

  > 폰트 지정 !!