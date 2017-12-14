# Day 06

- sinatra

  - fake_search

  - fake_op.gg

    ```html
    <form action="http://www.op.gg/summoner/" method="get">
    	<input type="text" name="userName">
    	<input type="submit" value="검색하기">		
    </form>
    ```

    > form 태그 만들기

    ```ruby
    @encoded = URI.encode(@id)
    ```

    > 한글 URI 인코딩

    ```ruby
    File.open('log.txt',"a+") do |f|
    	f.write("#{@id}, #{@tier.text}, #{@win.text}, #{@lose.text} \n")
    end

    CSV.open('log.csv', "a+") do |c|
    	c << [@id, @tier.text, @win.text, @lose.text, Time.now.to_s]
    end
    ```

    > 로그 파일 만들기 
    >
    > txt는 string으로 넣어야 한다 !!
    >
    > csv는 배열로 넣으면 된다 !!

    ```erb
    <input type="radio" name="">
    ```

    > radio 하나만 선택 할 수 있는 것 !!