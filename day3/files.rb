# 폴더는 files2
# 파일 30개를 만들어 주세요 
# 파일 제목은 1.txt 2.txt
# 파일 내용에 좋은 아침 입니다. 

Dir.chdir("files2")

30.times do |n|
	n = n+1
	File.open("#{n}.txt","w") do |file| file.write("좋은 아침 입니다. #{n}")
	end
end