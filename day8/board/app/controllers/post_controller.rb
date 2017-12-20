class PostController < ApplicationController
  def index
    @posts = Post.all
  end
  def new

  end
  def create
    @title = params[:title]
    @content = params[:content]

    # @post = Post.new
    # @post.title = @title
    # @post.content = @content
    # @post.save

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
  def destroy
    @id = params[:id]
    @post = Post.find(@id)

    @post.destroy
    redirect_to '/'
  end
  def edit
    @id = params[:id]
    @edit_post = Post.find(@id)
  ends
  def update
    @id = params[:id]
    @update_post = Post.find(@id)
    # @update_post.title = params[:title]
    # @update_post.content = params[:content]
    # @update_post.save

    @update_post.create(
      title: params[:title],
      content: params[:content]
    )
    redirect_to "/post/show/#{@id}"
  end
end
