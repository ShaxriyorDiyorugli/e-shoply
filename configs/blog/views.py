from django.shortcuts import render
from .models import Article, Category

def index(request):
    return render (request, template_name='blog/index.html')

