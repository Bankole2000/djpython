from django.shortcuts import render
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


def home(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)

def about(request): 
  return render(request, 'blog/about.html', {'title': 'About.html'})


# Create your views here.
