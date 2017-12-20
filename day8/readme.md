# day08

-  우분투 켜기

  ```bash
  vagrant up
  vagrant ssh
  cd /
  cd vagrant/likelion
  ```

- 프로젝트 만들기

  ```bash
  rails new [프로젝트명]
  cd [프로젝트명]
  rails g controller home index
  ```

- MVC 이해하기

  - 진행 ~

- layout 안 쓰기

  ```ruby
    def welcome
      @user = params[:user]
      render :layout => false
    end
  ```

- 시나트라로 했던 것 복습 !!

- board (부트스트랩 쓰기)

  -  모델 만들기

  ```bash
  rails g model post 
  ```

  > 포스트라는 모델 만들기

  ```ruby
  class CreatePosts < ActiveRecord::Migration
    def change
      create_table :posts do |t|
          t.string :title
          t.string :content
          
        t.timestamps null: false
      end
    end
  end
  ```

  ```bash
  rake db:migrate
  ```

  > db만들기!!

  ```ruby
  gem 'rails_db'
  ```

  > db 확인 가능 !!

  - CRUD

    ```ruby
        # @post = Post.new
        # @post.title = @title
        # @post.content = @content
        # @post.save

        Post.create(
          title: @title
          content: @content
        )
    ```

    > 주석한 부분과 아래 부분이 완전히 똑같은 문법이다.

    ```ruby
        # @update_post.title = params[:title]
        # @update_post.content = params[:content]
        # @update_post.save

        @update_post.create(
          title: params[:title],
          content: params[:content]
        )
    ```

    > update도 동일 !!

    - 한번에 만들기 !!

      ```bash
      rails g scaffold post title content
      rake db:migrate
      ```

      > 하면 CRUD 끝 !!