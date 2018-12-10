from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# request 就是 Django 为我们封装好的 HTTP 请求，它是类 HttpRequest 的一个实例
def index(request):
    # 定义字典,需要传递给index.html的模板变量中
    context = {
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
            }
    return render(request, 'blog/index.html', context=context)