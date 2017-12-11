# Day 03

- Day 02 복습

  - 파일 만들기

  ```ruby
  Dir.chdir("files2")
  ```

  > 디렉토리 변경

  ```ruby
  30.times do |n|
  ```

  > 30번 반복

  ```ruby
  n = n+1
  ```

  > 0번 부터 29번이기 때문에 n에 +1을 해준다.

  ```ruby
  File.open("#{n}.txt","w") do |file| file.write("좋은 아침 입니다. #{n}")
  ```

  > File이라는 것을 사용한다. F는 반드시 대문자
  >
  > open 두번째 속성의 종류는 
  >
  > r - 읽기 전용. 파일이 있어야 합니다.
  >
  > w - 쓰기 위해 빈 파일을 만듭니다.
  >
  > a  - 파일을 추가 합니다. 파일이 없으면 파일이 만들어 집니다.
  >
  > r+ - 읽기 및 쓰기 업데이트 파일을 엽니다. 파일이 있어야 합니다.
  >
  > w+ - 읽기와 쓰기 모두를 위한 빈 파일을 만듭니다.
  >
  > a+ - 읽기 및 추가를 위해 파일을 만듭니다. 파일이 없으면 작성 됩니다.



- Day 03 시작

  - 파일 이름 바꾸기

  ```ruby
  files = Dir.entries(Dir.pwd).reject {|name| name[0] == "."}
  ```

  > entries => 넣어라
  >
  > Dir.pwd => 현재 디렉토리
  >
  >  reject {|name| name[0] == "."}
  >
  > 점(.)으로 시작하는 폴더를 제외한 모든 폴더를 files에 넣겠다.
  >
  > . 은 현재 폴더
  >
  > ..은 상위 폴더를 의미한다.

  ```ruby
  File.rename(file, "mulcam"+file)
  ```

  >  name(old_name, new_name)

  ​

  - stock(https://github.com/tyrauber/stock_quote)

  ```bash 
  gem install stock_quote
  ```

  > ruby gem => 루비는 보석에 일종이다. 루비로 짜여 있는 코드의 집합. 쉽게 쓰게 만들어진 것
  >
  > rubygems.org

  ```ruby
  require "stock_quote"
  ```

  > require와 상관 없이 다 포함 해버리면 속도 상의 문제나 불편함이 있기 때문에 따로 설치한 gem은 require로 불러줘야 한다.

  ```ruby
  __END__
  ```

  > 루비 코드가 끝났다고 의미
  >
  > 밑은 메모장과 같다고 생각해도 된다.

  ```ruby
  DATA.each do |company|
  	company.chomp!
  ```

  > DATA => __END__ 밑에 값을 가져옴
  >
  > chomp가 필요 !!

  ​

  - bundle 사용

  ```bash
  gem install bundler
  ```

  > 가장 많이 쓰는 gem
  >
  > gem을 쉽게 깔기 위해서 사용
  >
  > Gemfile (G는 대문자) 파일 만들기
  >
  > source 'https:rubygems.org' 여기서 받아 올 것을 명시

```bash
ruby>bundle
```

- - 환율 정보

```ruby
require 'eu_central_bank'
```

```ruby
amount.to_i
```

> integer 값으로 변환
>
> to_s string으로
>
> to_f float 값으로
>
> to_r 실수 값으로

```ruby
if amount.is_a?(String)
```

> String이면 실행한다.

```ruby
ARGV.each do |company|
```

> 넣어준 값을 배열에 넣는다.

- - 날씨

```ruby
require 'forecast_io'
```

- - 좌표 받아오기

```ruby
require 'geocoder'

print '어디가 궁금하세요? : '
location = gets.chomp!

loCord = Geocoder.coorinates(location)

puts loCord
```

> 값 입력 받기 
>
> get만 쓰면 되지만 \n을 없애기 위해서 chomp! 를 사용

```bash
s.class
```

> 가지고 있는 자료형이 무엇인지 알 수 있다.

