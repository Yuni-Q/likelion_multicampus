# 1 1부터 100 까지 돌면서
  #2 숫자가 3의 배수면  Fizz
  #3 5의 배수면 Buzz
  #4 둘 다의 배수면 FizzBuzz
  #5 그 외에는 그냥 숫자

  for i in 1..100
    if((i%3===0)&&(i%5===0))
       puts "FizzBuzz"
    elsif ((i%3)===0)
      puts "Fizz"
    elsif ((i%5) ===0)
      puts "Buzz"
    else
      puts i
    end
  end

# (1..50).each do |number|
# end
