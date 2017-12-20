# day09

- CRUD 복습 (1시간 각자 만들고 오전 따라 했음. 난 안 했음...;;)

  ```bash
  rails d controller [controller명]
  ```

  > rails g 한 것을 없앨 때 사용 !!

  ```ruby
  before_action : set_post, only [:show, :edit, :destroy]
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

