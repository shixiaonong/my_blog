from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# request 就是 Django 为我们封装好的 HTTP 请求，它是类 HttpRequest 的一个实例
from .models import Post


def index(request):
    # 文章列表按照创建时间的新旧顺序，最新在最前面
    post_list = Post.objects.all().order_by('-created_time')

    context = {'post_list': post_list}

    return render(request, 'blog/index.html', context=context)
