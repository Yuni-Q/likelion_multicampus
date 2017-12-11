# files 디렉토리로 옮겨
Dir.chdir("files") 

# 30개의 파일을 만듭니다.
# 1.txt ~ 30.txt
# 1.txt => 1번째 내용
# 30.txt => 30번쨰 내용
# ruby file new

(1..30).each do |number| 

	File.open("#{number}.txt", "a") {|f| f.write("#{number}번째 내용") }

end

# r- 읽기 전용. 파일이 있어야합니다.
# w - 쓰기 위해 빈 파일을 만듭니다.
# a - 파일에 추가합니다. 파일이 없으면 파일이 만들어집니다.
# r+- 읽기 및 쓰기 업데이트 파일을 엽니 다. 파일이 있어야합니다.
# w+ - 읽기와 쓰기 모두를위한 빈 파일을 만듭니다.
# a+- 읽기 및 추가를 위해 파일을 엽니 다. 파일이 없으면 작성됩니다.

# 30.times do |n|
# 	n = n+1
# 	File.open(n.to_s+".txt", "w") do |file| file.write(n.to_s+"번째 내용입니다.")
# 	end
# end