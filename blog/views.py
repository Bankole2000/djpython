from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.core.signals import request_finished
# from django.dispatch import receiver
# from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView,
  UpdateView,
  DeleteView
)
from .models import Post
# from django.http import HttpResponse 

# posts = [
#   {
#     'author': 'Bankole Esan',
#     'title': 'Awesome Title',
#     'content': 'First Post content',
#     'date_posted': 'August 27, 2019'
#   },
#   {
#     'author': 'James Bond',
#     'title': 'Tomorrow Never Dies',
#     'content': 'Second Post content',
#     'date_posted': 'August 28, 2019'
#   }
# ]


# def home(request):
#   context = {
#     'posts': Post.objects.all()
#   }
#   return render(request, 'blog/home.html', context)

class PostListView(ListView): 
  model = Post
  template_name = 'blog/home.html' 
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 2

class UserPostListView(ListView): 
  model = Post
  template_name = 'blog/user_posts.html' 
  context_object_name = 'posts'
  paginate_by = 2

  def get_queryset(self): 
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView): 
  model = Post

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
  model = Post
  fields = ['title','content']
  success_message = '☑️ 📖✍  Post has been Created 👍 '

  def form_valid(self, form): 
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView): 
  model = Post
  fields = ['title','content']
  success_message = '☑️ 📖✍  Post has been Updated 👍 '

  def form_valid(self, form): 
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self): 
    post = self.get_object()
    if self.request.user == post.author: 
      return True
    return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
  model = Post
  success_url = '/'
  # success_message = '📖 Post has been Deleted 💣 ✖️ 👍 '

  def test_func(self): 
    post = self.get_object()
    if self.request.user == post.author: 
      messages.warning(self.request, '⚠ This Post will be Deleted 💣 ✖️ 👍 ')
      return True
    return False

def about(request): 
  return render(request, 'blog/about.html', {'title': 'About.html'})


# Create your views here.
