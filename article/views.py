# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from article.models import Article

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})
def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
