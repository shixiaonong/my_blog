from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    # 在admin站点中能够显示的字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)