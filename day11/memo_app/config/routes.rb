Rails.application.routes.draw do
 
  get '/about' => 'hello#about'

  get '/help' => 'hello#help'

  root 'posts#index'

  # get '/posts/new' => 'posts#new'
  
  # get '/posts/edit' => 'posts#edit'
  
  # get '/posts' => 'posts#index'
  
  # get '/posts/:id' => 'posts#show'
  
  # post '/posts' => 'posts#create'

  resources :posts
end
