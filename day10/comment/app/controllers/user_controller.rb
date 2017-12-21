class UserController < ApplicationController
  def new
  end

  def create
    @email = params[:email]
    @password = params[:password]

    User.create(
      email: @email,
      password: @password
    )
    redirect_to '/'
  end

  def login
    if session[:user_id]
      flash[:notice] = "로그아웃부터 해라."
      redirect_to '/'
    end
  end

  def login_process
    @email = params[:email]
    @password = params[:password]

    @user = User.find_by(email: @email)
    if User.exists?(email: @email)
      if @user.password == @password
        session[:user_id] = @user.id
        flash[:green] = "안녕"
        redirect_to '/'
      
      else
        flash[:notice] = "비밀번호 없다"
      end
    else
      flash[:notice] = "아이디 없다"
      redirect_to "/user/new"
    end 

  end

  def logout
    if session[:user_id]
      session.clear
      flash[:notice] = "로그아웃 되셨습니다."
    else 
      flash[:notice] = "로그인이나 해라."
      redirect_to '/user/login'
    end
  end
end
