class PostController < ApplicationController
  before_action :authenticate_user, except: :index
  def index
  	@posts = Post.all.order("title")
  end

  def new
  end

  def create
  	@title = params[:title]
  	@content = params[:content]

  	Post.create(
  		title: @title,
  		content: @content
  	)

  	redirect_to '/'
  end
  def show
  	@id = params[:id]
  	@post = Post.find(@id)
  end
  def create_reply
  	@content = params[:content]
  	@post_id = params[:id]

  	Reply.create(
  		content: @content,
  		post_id: @post_id
  	)

  	redirect_to :back #rails 4
  	#redirect_back(fallback_loction: post_path) #rails 5
  	
  end

  def edit
  	@id = params[:id]
  	@post = Post.find(@id)
  end
  def update
  	@id = params[:id]
  	@title = params[:title]
  	@content = params[:content]
  	@post = Post.find(@id)

  	@post.update(
  		title: @title,
  		content: @content
  	)
  	redirect_to '/'
  	
  end
  def destroy
  	@id = params[:id]
  	@post = Post.find(@id)

  	@post.destroy

  	redirect_to '/'
  	
  end
  	
end
