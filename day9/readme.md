# day09

- CRUD 복습 (1시간 각자 만들고 오전 따라 했음. 난 안 했음...;;)

  ```bash
  rails d controller [controller명]
  ```

  > rails g 한 것을 없앨 때 사용 !!

  ```ruby
  before_action :set_post, only: [:show, :edit, :destroy, :update]
  private
  def set_post
    @id =params[:id]
    @post = Post.find(@id)
  end
  ```

  ​

- makedown

  > html 태그 사용 가능 !!
  >
  > ---- => 줄 긋기
  >
  > \![](이미지 url) => 이미지 첨부 !!
  >
  > \<img src="이미지url"> => 이미지 첨부 2 !!-	

- 명령어 저장

  ```bash
  cd ~
  ls -a #숨김 파일 보기
  vi .bashrc #파일 켜기
  i #입력창으로 들어가기 insert
  alisas rs='rails s =b 0.0.0.0' #rs라는 명령어로 뒤에껄 실행하겠다.
  esc #입력을 종료하겠다.
  :wq #쓰고 나가라 !
  source ~/.bashrc #명령어 업데이트
  rs #이제 rs만 치면 rails s =b 0.0.0.0가 실행 됨 
  ```
    > window만 가능?;;

- 전송 방법

  - get 말고도 post/delete/put/patch 등등 많음 (CRUD에 매칭 됨)

  - post 사용

    ```ruby
    <form action="/post/create" method="post">
    ```

    > form에 method로 post를 준다

    ```ruby
    post 'post/create'
    ```

    > routes에서 post 방식으로 지정해 준다.

    ```ruby
    # protect_from_forgery with: :exception
    ```

    > application_controller에서 위에 문장을 주석 처리 해준다.
    >
    > CSRF공격 예방 하는 건데 주석 처리
    >
    > ```ruby
    > <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>">
    > ```
    >
    > 위의 방식은 안전하지 않기 때문에 폼 마지막에 위와 같이 넣어 주면 된다.

  - delete

    ```ruby
    <a data-confirm="정말 지울꺼니?" data-method="delete" href="/post/destroy/<%= p.id %>">삭제</a>
    ```

- 로그인 만들기

  - gem 'digest'

    > 비밀번호 암호화를 위해 쓰는데
    >
    > 위에껀 이미 뚫림 그래도 이해를 위해 쉬운거 사용

    ```ruby
        require 'digest'

        @email = params[:email]
        @password = params[:password]

        hidden_password = Digest::MD5.hexdigest(@password)                                   
    ```

  - login_process

    ```ruby
      def login_process
        @email = params[:email]
        @password = params[:password]

        user = User.find_by(email: @email)

        # user가 있는지 먼저 검사
        if User.exists?(email: @email)
          # 아이디와 패스워드가 일치 하면 로그인
          # 일치하지 않으면 로그인 불가능

          if user.password == Digest::MD5.hexdigest(@password)
            session[:user_id] = user.id #세션에 값 넣기
            redirect_to '/'
          end
        end
    ```

    ```ruby
      def index
        if session[:user_id]
          @email = User.find(session[:user_id]).email
        end
      end
    ```

    > 메인에서 email 보여주기 !!

    ```ruby
      def logout
        session.clear
        redirect_to '/'
      end
    ```

    > 로그 아웃 !!
    >
    > 세션 지우기 !!

- 쿠키와 세션

  - 쿠키는 사용자가 가지고 있다 (광고는 쿠키값에 따라 보인다)
  - 세션은 서버가 가지고 있다