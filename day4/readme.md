# Day 04

- git 설치

  > ls => dir 하위 폴더
  >
  > cd => cd 폴더 이동
  >
  > pwd => 현재폴더

- github에 올리기

- Sinatra  웹 프로그래밍

  ```ruby
  require 'sinatra'

  get '/' do
  	"Hack your life"
  end
  ```

  > localhost:4567을 만듬
  >
  > 정말 간단하게 웹 페이지를 만듬 (외부에서 접근은 안 됨)
  >
  > 레일즈보다 가벼운 프레임 워크

  ```ruby
  get '/welcome/:name' do
  	name = params['name']
  	"#{name}님 반갑습니다."
  end
  ```

  > 여러 주소 받기

  ```ruby
  get '/' do
  	"<h1>점심 빨리 먹고 싶다</h1>"
  end

  get '/intro' do 
  	send_file "intro.html"
  end
  ```

  > html 코드를 쓸 수 있고
  >
  > html 파일을 불러 올수도 있다 (send_file)

  ```ruby
  get '/outro' do 
  	erb :outro
  end
  ```

  > 인베디드 루비 (erb)

  ```ruby
  get '/lunch' do
  	@menus = ['kimchi', '20','GS','pizz']
  	@eats = ['드세요','먹어라','먹던가']
  	@menu = @menus.sample + @eats.sample
  	erb :lunch
  end
  ```

  > 변수 던지기 !!

  ```erb
  <h1><%= @menu %></h1>
  <img src=<%= @url %>>
  ```

  > 변수 받기 !!

  ```ruby
  menus = ["김밥","피자","짜장면","칼국수"]
  menu_url = {
    "key1" => "value1",
    :key2 => "value2"
    key3: "value3"
  }

  @menu = menus.sample
  @url = menu_url[@menu]
  ```

  > Hash 사용하기
  >
  > hash 사용 법은 1,2,3, 순으로 발전해 왔으나 무엇을 쓰던 상관 없다