# 폴더 안으로 들어 갑니다.
Dir.chdir("files2")
# 폴더 안을 돌면서 파일 이름을 가져 옵니다. 

files = Dir.entries(Dir.pwd).reject {|name| name[0] == "."}
files.each do |file|
	File.rename(file, "mulcam"+file)
end 

# 각각의 파일을 1.txt => mulcam1.txt

