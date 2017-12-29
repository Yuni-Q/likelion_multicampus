# Day 15

- brew update

- vim_git

  ```Bash
  vim hello_git.text
  ```

  > 나가는 방법
  >
  > :q
  >
  > ​
  >
  > 쓰는법
  >
  > i
  >
  > ​
  >
  > 한줄 밑에서 시작
  >
  > o
  >
  > ​
  >
  > 특정 모드를 끝낼 때는 esc
  >
  > 저장
  >
  > :w
  >
  > ​
  >
  > 저장 안하고 끄는법
  >
  > :q!
  >
  > ​
  >
  > 한번에 2개도 가능
  >
  > :wq
  >
  > ​
  >
  > wq 한글자로
  >
  > :x
  >
  > ​
  >
  > vi가 진화한게 vim

- 명령어

  ```bash
  ls
  하위 폴더

  ls -a
  숨김 폴더

  ls -l
  길게 나옴

  ls -t 
  시간 순

  ls -al
  다 보여주면서 길게 보여줘라

  rm test.text
  삭제

  mk dir test
  폴더 만들기

  	d 디렉토리 폴더라는 뜻
  	rwx 권한 3번 반복
  	관리자 유저 게스트
  	읽기(r) 쓰기(w) 실행(x)

  	chmod 774 hello_git
  	권한 변경
  	4 2 1 2진수라서

  touch a 
  a라는 파일 만듬

  rm 파일 이름
  파일 지우기
  rm -r 폴더이름
  폴더 지우기 (하위에 파일있으면 못 지움)
  rm -f
  강제 삭제
  rm -rf
  폴더와 하위파일 다 지우기

  ```

- git

  ```bash
  git config --global core.editor vim
  git commit
  ```

  > vim으로 메세지 입력 가능하게 된다 !!

  ```bash
  git diff
  ```

  > 변경 사항 알려 준다 !!