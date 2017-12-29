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
  > ㅇ
  >
  > ​
  >
  > 한줄 삭제
  >
  > dd

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
  >
  > 차이가 없으면 아무것도 보여주지 않는다

  ```bash
  git log
  ```

  > 버전 보기

  ```bash
  git status
  ```

  > 변동 파일 알려준다

  ```bash
  git reset HEAD 파일이름
  ```

  > add .에서 파일을 빼준다
  >
  > Unstage하며, HEAD commit으로 commit만 바꾼다
  >
  > git status 치면 명령어 나온다

  ```bash
  vim .gitignore
  파일이름
  /폴더이름/*
  ```

  > 저장하고 나오면 된다
  >
  > *은 모든 파일

  ```bash
  mv 옮길파일 옮길폴더
  ```

  > 파일 옮기기

  ```bash
  git HEAD
  ```

  > 마지막으로 뭐했는지 체크 할 수 있다

- 버전 관리

  ```bash
  git checkout HEAD .
  git checkout HEAD 파일명
  ```

  > 마지막 커밋으로 돌아간다
  >
  > HEAD commit 상태로 파일로 되돌림

  ```bash
  git checkout HEAD~숫자 <파일명 or .>
  ```

  > HEAD 기준으로 n단계 전 commit 상태로 되돌림 

  ```bash
  git reset 커밋버전네임
  ```

  > commit 상태만 커밋버전네임 상태로 되돌림
  >
  > 파일은 그대로 있음

  ```bash
  git checkout 커밋버전네임
  ```

  > 커밋버전네임 상태로 파일만 되돌림
  >
  > 뒤에 파일 있으면 파일만 없으면 전체 !!

- git push

  ```bash
  echo "# aa" >> README.md
  ```

  > readme 없으면 만들기

  ```bash
  cat 파일명
  ```

  > 파일 내용 나온다

  ```bash
  git pull
  ```

  > 가져오기

  ```bash
  echo 'Yap' >> readme.md
  ```

  > Yap이 readme.md 맨 마지막 줄에 들어감

- bash 바꾸기 (zshell)

  ```bash
  brew install zsh
  which zsh
  sudo vi /etc/shells
  (wcich zsh 했던 결과값을 안에 넣는다)
  chsh -s 'which zsh'
  (oh my zsh 검색해서 젤 위에 깃에 접속)
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
  cd ~
  vi .zshrc
  테마를 refined (여러개 있음)
  source .zshrc
  cd 하고 taptaptaptap
  ```

  ```bash
  ga . => git add .
  gc -m "hello" => git commit
  ```

  ​

  ​