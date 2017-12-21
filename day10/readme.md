# day10

- 댓글 만들기

  ```bash
  div#idasdlk;asd #=> <div id="asdlk;asd" 됨
  div.classasd #=> <div class="asd" 됨
  ```

  - post 만들기

    - Bootstrap 사용

      ```ruby
      <%= render 'layout/header' %>
      ```

      > layout 폴더에 \_header.html.erb 만들고 부르기 

  - 댓글 만들기

    - 게시글과 댓글은 1 : n 관계

    ```bash
    rails g model reply content post_id:integer
    ```

    > Post_id를 Integer로 만들겠다.
    >
    > model명과 프로젝트명은 같을 수 없다.

    ```ruby
    class Post < ActiveRecord::Base
    	has_many :replies
    end
    ```

    > app/model/Post.rb
    >
    > post는 많은 replies를 가지고 있다

    ```ruby
    class Reply < ActiveRecord::Base
    	belongs_to :post
    end
    ```

    > app/model/reply.rb
    >
    > reply는 하나는 post를 가지고 있다

    ```ruby
    redirect_to :back #rails 4
    #redirect_back(fallback_loction: post_path) #rails 5
      	
    ```

    > 작성하기 페이지로 돌아가기 

    - gem 'faker'

      ```ruby
      10.times do
      Post.create(
      	title: "this is seeds",
      	content: "this is also seeds"
      	)
      end
      ```

      ```bash
      rake db:seed
      ```

      > 하면 DB에 만들어짐

      ```ruby
      10.times do
      Post.create(
      	title: Faker::Pokemon.name,
      	content: Faker::Pokemon.location
      	)
      end
      ```

      > 포켓몬

  - 정렬

    ```ruby
      def index
      	@posts = Post.all.order("title")
      end
    ```

    > title로 정렬
    >
    > 대문자 > 소문자 > 한글 순이다

  - 로그인 붙이기

  - 플래시 붙이기

    ```ruby
      def login_process
        @email = params[:email]
        @password = params[:password]

        @user = User.find_by(email: @email)
        if User.exists?(email: @email)
          if @user.password == @password
            session[:user_id] = @user.id
            flash[:green] = "안녕"
            redirect_to '/'
          
          else
            flash[:notice] = "비밀번호 없다"
          end
        else
          flash[:notice] = "아이디 없다"
          redirect_to "/user/new"
        end 

      end
    ```

    > controller에  flash 넣기

    ```ruby
    <% if flash[:notice] %>
      <div class="alert alert-danger" role="alert">
        <%= flash[:notice] %>
      </div>
    <% elsif flash[:green] %>
      <div class="alert alert-success" role="alert">
        <%= flash[:green] %>
      </div>
    <% end %>
    ```

    > 원하는 위치에 넣기 !!

  - 권한 주기

    ```ruby
    def current_user
      	@user ||= User.find(session[:user_id]) if User.exists? && session[:user_id]
      end

      helper_method :current_user

      def authenticate_user
      	unless current_user
      		flash[:notice] = "로그인을 해야 게시판을 볼수 있습니다."
      		redirect_to '/user/login'
      	end
      end
    ```

    > applicaion_controller에 작성
    >
    > ||= => 비었으면 넣어라
    >
    > if 한줄 코딩 방법
    >
    > helper_metthod 사용

    ```ruby
      before_action :authenticate_user, except: :index
    ```

    > index 빼고는 다 권한 설정을 받아랏 !! 

- Typora

  > 강조 \**강조할 말**


  > 하이라이트 \==하이라이트할말==
  >
  > 설정에서 추가하고 다시 시작해야 적용이 된다

  ​







