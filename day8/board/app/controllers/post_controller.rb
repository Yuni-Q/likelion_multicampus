class PostController < ApplicationController
  before_action :set_post, only: [:show, :edit, :destroy, :update]

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
  end
  def destroy
    @post.destroy
    redirect_to '/'
  end
  def edit

  end
  def update
    # @update_post.title = params[:title]
    # @update_post.content = params[:content]
    # @update_post.save

    @post.update(
      title: params[:title],
      content: params[:content]
    )
    redirect_to "/post/show/#{@id}"
  end
  private
    def set_post
      @id =params[:id]
      @post = Post.find(@id)
    end
end
