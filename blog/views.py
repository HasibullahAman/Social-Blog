from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



posts = [
    {
        'author': 'Hasibullah Aman',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2024'
        },
    {
        'author': 'Nawidullah Aman',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 30, 2024'
    }
]

def home(request):
    context = {
        'post': posts 
    }
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')

# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")


# def about(request):
#     return HttpResponse("<h1 style = background-color:red;>Blog About</h1>")


