from django.shortcuts import render
from .models import Article, Category

def index(request):

    context = {
        'title':'Tech Box'
    }

    return render(request, 'blog/index.html', context)

