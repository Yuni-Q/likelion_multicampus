# Day 18

- 카카오 챗봇 만들기

- 카카오톡 관리자 센터에서 새 플러스 친구 만들기

- 키보드 필요함

  - ```ruby
    예제
    {
      "type" : "buttons",
      "buttons" : ["선택 1", "선택 2", "선택 3"]
    }
    ```

  - ```ruby
      	home_keyboard = {
      		type: "text"
    		# 우선 type를 text로 만들어 보자
    	}
    ```

  - ```ruby
    # routes.rb
      get '/keyboard' => 'kakao#keyboard'

      post '/message' => 'kakao#message'
    # 라우팅은 api 설정에 맞춰 바꿔준다
    ```

- 메아리 쳐주는 친구 만들기

  - ```ruby
      def message
      	user_message = prams[:content]

      	return_message = {
      		:message => {
      			:text => user_message
      		},
      		:keyboard = {
      			:type => "text"
      		}
      	}
      end
    ```

  - ```ruby
    # 확인을 위해 routes에
      get '/message' => 'kakao#message'
    # 추가
    ```

  - http://localhost:3000/message?content=안녕하세요

  - ```json
    # 결과
    {"message":{"text":"안녕하세요"},"keyboard":{"type":"text"}}
    ```

- heroku 배포

  - ```ruby
    # Gemfile
    #gem 'sqlite3'
    gem 'sqlite3', :group => :development
    gem 'pg', :group => :production
    gem 'rails_12factor', :group => :production
    ```

  - 그리고 `/config/database.yml`파일도 수정을 해주세요

    ```Ruby
    # 변경전
    # production:
    #   <<: *default
    #   database: db/production.sqlite3

    # 변경후  
    production:
      <<: *default
      adapter: postgresql
      encoding: unicode
    ```

  - 안되면

  - Brew update

  - Brew install postgresql

  - (Sudo apt-get install postgresql) 우분투는 위에 2개가 아니라

  - gem install heroku

  - heroku login

  - 리퀘스트가 없다고 하면 gem install request

  - 다시 gem install heroku

  - Heroku create "이름"

  - git init

  - git add .

  - git commit -m "메세지"

  - git push heroku matser

  - 안되면

  - git create

  - git push heroku master

- 카카오 api형 만들기

  - 주소넣고 만들면 된다
  - 공개 설정 해 주고
  - 실행 해주면 된다

- 다른 기능 추가

  - ```ruby
      	if user_message = "메뉴"
      		menus = ["20cmd","asd","qwe","zxc"]
      		user_message = menus.sample
    ```

- 고양이 사진

  - ```ruby
    gem 'nokogiri'
    gem 'rest-client'
    ```

  - 이하 생략

- 영화 제목 이미지 평점 가져오기 !!

- 모듈 사용하기 !! ( help 안에 Pares 안에 Moudle 만들어서 사용 )

- 다양하게 구성해 보세요 !!