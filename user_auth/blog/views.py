from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'Anjan',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'May 27, 2022'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'May 28, 2022'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  

 