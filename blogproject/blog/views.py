from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# request 就是 Django 为我们封装好的 HTTP 请求，它是类 HttpRequest 的一个实例
def index(request):
    return HttpResponse('欢迎访问我的博客首页！')