import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.


# request 就是 Django 为我们封装好的 HTTP 请求，它是类 HttpRequest 的一个实例
from .models import Post


def index(request):
    # 文章列表按照创建时间的新旧顺序，最新在最前面
    post_list = Post.objects.all().order_by('-created_time')

    context = {'post_list': post_list}

    return render(request, 'blog/index.html', context=context)


def detail(request, pk):
    # 其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，
    # 如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})

