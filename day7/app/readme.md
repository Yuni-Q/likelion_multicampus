# day 07

- rails 시작

  ```ㅠㅁ노
  rails new app
  rails s -b 0.0.0.0
  ```

  > app라는 프로젝트를 만들겠다.
  >
  > s 프로젝트를 실행 시키겠다.

  ```bash
  rails g controller home
  ```

  > home 이라는 controller를 만들겠다. (generated)

  ```ruby
  get 'home/index' => 'home#index'
  get 'home/index'
  ```

  > 첫번째 줄과 같이 앞뒤가 같으면 두번째 줄처럼 작성해도 된다.
  >
  > 또한 render를 안해도 되게 도와준다.