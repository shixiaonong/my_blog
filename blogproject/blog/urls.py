from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页的路由, 并且给这个视图函数起了一个别名
]