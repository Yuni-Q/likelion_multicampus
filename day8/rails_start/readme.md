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