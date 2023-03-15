from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Me, Myself, and I',
        'title': 'Blog Post 1',
        'content': 'My First Post Content',
        'date_posted': 'August 21, 2022'
    },
    {
        'author': 'Me, Myself, and I',
        'title': 'Blog Post 2',
        'content': 'My Second Post Content',
        'date_posted': 'August 21, 2022'
    },
]

def home(request):
    context = {
        'title': 'Home Page',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})