# Day05

- Day04 복습

  - sinatra

    > 폴더를 만드는 것은 보기 편한게 아니라
    >
    > 폴더 하나당 프로젝트 하나 !!
    >
    > 프로젝트 단위로 움직인다 !!

  - 리눅스 명령어

    > mkdir sample => sample이라는 폴더 만들기
    >
    > rm => 삭제 (파일)
    >
    > rm -r sample => 디렉토리 삭제
    >
    > rm -rf sample => 하위 항목까지 모드 삭제 
    >
    > touch => 새 파일을 만들기
    >
    > ctrl+l => 클리어 (bash창 클리어)
    >
    > mv dinner/ sinatra/ => dinner를 sinatra 안으로 옮기겠다.

  - 영화 받아 오기

    ```ruby
    Array.new
    ```

    > 새로운 배열 만들기 !!

    ```ruby
    require 'nokogiri'
    require 'open-uri'
    ```

    > open-uri는 기본적으로 있다
    >
    > uri 밑에 urn이랑 url 이 있다고 한다. (잘 모르겠다.)

    ```ruby
    @url = 'http://movie.naver.com/movie/running/current.nhn'
    @doc = Nokogiri::HTML(open(@url),nil,'UTF-8')
    @movie_title = Array.new
    @doc.css("ul.lst_detail_t1 dt a").each do |title|
    	@movie_title << title.text
    end

    @movie = @movie_title.sample
    ```


    erb :movie
    ​```

  - scraper

    ```ruby
    require 'mechanize'

    agent = Mechanize.new
    agent.user_agent_alias = 'window chrom'

    page = agent.get('https://www.amazon.com')
    ```


    ​```

  - 이사 하기 !!

    ```bash
    vagrant up
    vagrant ssh
    ```

    > up = > vagrant 깨우기
    >
    > ssh => 들어가기

    - go rails 가서 따라 하기 !!

      > vagrant는 ruby 버전 옮겨 다니면서 쓸 수 있다.	

      ```bash
      rbenv global 2.4.2
      ```

      > 루비 버전을 2.4.2를 기본 설정으로 하겠다 !!