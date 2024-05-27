from django.shortcuts import render

posts = [
    {
        'author': 'Fernando',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 27, 20224'
    },
    {
        'author': 'Diogo',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 28, 2024'
    }
]

def home(request):
    context = {
        'title': 'teste',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})