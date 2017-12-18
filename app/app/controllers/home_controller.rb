class HomeController < ApplicationController
  def index
    @lotto = [*1..49].sample(6)
  end

  def hello
    @lunch = ["중국집","칼국수","20층","김밥","편의점"].sample
  end
end
