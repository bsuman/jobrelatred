from django.shortcuts import render
from django.http import HttpResponse

f_post = [
    {
        "author": 'Suman Bidarahalli',
        "title": 'My Fav Walnutbread Recipe',
        "content": 'https://www.seitenbacher.de/rezepte/brot-br%C3%B6tchen/herbstliches-walnuss-brot',
        "date_posted": 'February 7, 2023'
    },
    {
        "author": 'Ivo Ernst',
        "title": 'My Fav Schweinebraten Recipe',
        "content": 'https://www.chefkoch.de/rezepte/1733131282370799/Einfacher-Schweinebraten.html',
        "date_posted": 'February 7, 2023'
    }
]


# Function to handle traffic from homepage to the blog
def home(request):
    context = {
        'posts': f_post
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
