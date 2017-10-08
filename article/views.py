# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from article.models import Article
from django.http import Http404
# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})
def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
def detail(request,id):	
    try:
	post = Article.objects.get(id=str(id))
    except Article.DoNotExist:
	raise Http404
    return render(request,'post.html',{"post" : post})
def archives(request):	
    try:
	post_list = Article.objects.all()
    except Article.DoNotExist:
	raise Http404
    return render(request,'archives.html',{"post_list" : post_list, 'error': False})
def aboutme(request):
    return render(request,'aboutme.html')
