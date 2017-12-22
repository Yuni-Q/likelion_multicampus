# Day11

- git push시  아이디 비번 자동 설정

  > 계정 설정에서 컴퓨터 등록
  >
  > SSH keys 사용
  >
  > id_rsa.pub 파일에 내용 복사해서 넣기 !!

- git 사용법

  ```bash
  git init
  git add .
  git commit -m "first commit"
  git remote add origin https://~
  git push origin master
  ```

- 복습

  ```ruby
    def hello
    	render html: "Hack Your Life"	
    end
  ```

  > html로 메세지 보내 !!

  ```Ruby
  <ul class="nav navbar-nav vavber-right">
  					<li><%= link_to "Home", root_path %></li>
  					<li><%= link_to "Help", help_path %></li>
  					<li><%= link_to "About", abot_path %></li>
  </ul>
  ```

  > a 태그 대신 !!

  ```ruby
  gem 'bootstrap-sass'
  ```

  ```scss
  @import 'bootstrap-sprockets';
  @import 'bootstrap';
  ```

  > App/asseets/stylesheets.custom.scss 만들어서 넣기
  >
  > 이름 상관 없음
  >
  > 여기에 css 작성하면 된다

  ```js
  //= require jquery
  //= require bootstrap-sprockets
  //= require jquery_ujs
  ```

  > App/asseets/javascripts/application.js에 jQuery 사이에 넣기 !!
  >
  > 서버 다시 켜기

  ```erb
  <%= render 'layouts/header' %>
  ```

  > \_header.html.erb에 넣어서 부르기 !!

  > ORM이 있어서 SQL문을 안 쓰고 DB를 쓸 수 있다

  - Html 코드 ruby 코드로 대체하기

    ```Erb
    <!-- <form action="/posts/create" method="post">
    	<input type="text">
    	<input type="text">
    	<input type="submit">
    </form> -->

    <%= form_for(@post) do |f| %>
    	<%= f.text_field :title,lavel: '제목' %>
    	<%= f.text_area :content, lavel: '내용' %>
    	<%= f.submit %>
    <% end %>
    ```

    > controller에서 
    >
    > @post = Post.new 해줘야 함
    >
    > Routes.rb에 post '/posts' => 'posts#create'로 지정

    ```ruby
        def create
            # params['post'] #우리가 원하는 자료는 여기에 담겨 있다
            @post = Post.new
            @post.title = params['post']['title']
            @post.content = params['post']['content']
            @post.save

            render html: "저장완료"
            
        end
    ```

  - 꾸미기

    ```ruby
    gem 'bootstrap_form'
    ```

    > 이쁘게 꾸며 보자

    ```ruby
    <%= bootstrap_form_for(@post) do |f| %>
    	<%= f.text_field :title,lavel: '제목' %>
    	<%= f.text_area :content, lavel: '내용' %>
    	<%= f.submit %>
    <% end %>
    ```

    ```ruby
    gem 'tinymce-rails'
    ```

    > Application.js에 //= require tinymce-jquery
    >
    > Custom.scss에 @import 'rails_bootstrap_forms'

    - 입력 form

    ```ruby
    <%= bootstrap_form_for(@post) do |f| %>
    	<%= f.text_field :title,label: '제목' %>
    	<%= f.text_area :content, label: '내용', class: 'tinymce', rows: 15, cols: 120 %>
    	<%= tinymce %>
    	<%= f.submit %>
    <% end %>
      
      
    ```

    > 꺼낼 때 <%= @post.content.html_safe %> 해야 함 !!

    - Table 꾸미기

    ```ruby
    <div class="table-responsive">
    	<table class="table bale fil">
    		<thead>
    			<tr>
    				<th>Title</th>
    				<th>Content</th>
    			</tr>
    		</thead>
    		<% @posts.each do |post| %>
    		<tbody>
    			<td><%= post.title %></td>
    			<td><%= post.content %></td>
    		</tbody>
    		<% end %>
    	</table>
    </div>
    ```

    - Localhost:3000/rails/info 하면 라우팅 나옴
    - Path 설정

    ```ruby
      # get '/posts/new' => 'posts#new'
      
      # get '/posts/edit' => 'posts#edit'
      
      # get '/posts' => 'posts#index'
      
      # get '/posts/:id' => 'posts#show'
      
      # post '/posts' => 'posts#create'

      resources :posts
    ```

    > 밑에 한 줄이 위에 여러줄 포함 더 많은 기능을 제공해 준다.

    - resource하면 더 간단하게 redirect_to 할 수 있다

      ```ruby
      #redirect_to post_path(@post)
      redirect_to @post
      #위 2줄은 같은 명령어
      ```

    - Confirm

      ```ruby
      <%= link_to '삭제하기', post_path, method: :delete, data: {confirm: '정말로 삭제합니다'} %>

      ```

    - Helper 이용

      ```ruby
      module ApplicationHelper
      	def icon(name)
      		content_tag('span', '', class: "glyphicon glyphicon-#{name}")
      	end
      end
      ```

      ```erb

      <%= icon 'pencil' %>
      <%= link_to '수정하기', edit_post_path %> 
      |
      <%= icon 'trash' %>
      <%= link_to '삭제하기', post_path, method: :delete, data: {confirm: '정말로 삭제합니다'} %>
      ```

    - gem 'local_time'

      ```ruby
      <td><%= <%= icon 'time' %><%= local_time(post.created_at) %></td>
      ```

      - gem 'rails-i18n

        > 다음 기회에 ...

    - 갯수 제한하기

      - Test/fixtures에서

        ```ruby
        <% 100.times do |i| %>
           post_<%= i+1 %>:
             title: <%= Faker::OnePiece.character %> 
             content: <%= Faker::Lorem.paragraph 20 %>
        <% end %>
        ```

        > rake db:fixtures:load

      - gem 'kaminari

        ```ruby
        def index
                @posts = Post.page(params['page']).per(20)
        end
        ```

        > post_controller

        ```ruby
         <%= paginate @posts %>
        ```

        > index.erb

    - 역순 정렬

      ```ruby
      @posts = Post.order(created_at: :DESC).page(params['page']).per(20)
      #@posts = Post.reverse.page(params['page']).per(20)
      ```

      ​