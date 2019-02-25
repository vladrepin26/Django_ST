from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'RepinV',
        'title': 'Post1',
        'content': 'First post content',
        'date_posted': 'August 26, 2018',
    },
    {
        'author': 'RepinD',
        'title': 'Post2',
        'content': 'Second post content',
        'date_posted': 'April 27, 2018',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
