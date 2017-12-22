class PostsController < ApplicationController
# Create
    ## 사용자가 글을 작성하는 화면
    def new
        @post = Post.new
    end
#Read
    ## 사용자에게 글 목록을 보여주는 화면
    def index
        @posts = Post.order(created_at: :DESC).page(params['page']).per(20)
    end
    ## 사용자가 글을 수정하는 화면
    def edit
        @post = Post.find params[:id]
    end
# Update
    ## 사용자가 글을 보는 화면
    def show
        @post = Post.find params[:id]
    end
    def create
        # params['post']
        @post = Post.new
        @post.title = params['post']['title']
        @post.content = params['post']['content']
        @post.save

        redirect_to @post
        
    end
    def update
        # params['post']
        @post = Post.find params[:id]
        @post.title = params['post']['title']
        @post.content = params['post']['content']
        @post.save

        #redirect_to post_path(@post)
        redirect_to @post
    end
#Destroy
    def destroy
        @post = Post.find params[:id]
        @post.destroy
        redirect_to root_path
    end
end
