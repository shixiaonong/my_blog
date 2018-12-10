from django.conf.urls import url
from . import views

app_name='blog'  # 指明这个urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页的路由, 并且给这个视图函数起了一个别名
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),  # 文章详情页的路由
]