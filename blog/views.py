from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')

# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")


# def about(request):
#     return HttpResponse("<h1 style = background-color:red;>Blog About</h1>")


