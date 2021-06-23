# Register your models here.

from django.contrib import admin

from .models import *

admin.site.site_header = '博客管理后台'
admin.site.site_title = '博客管理'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ('id', 'category', 'title', 'recommend', 'user', 'views', 'create_time')

    # 满50条数据就自动分页
    list_per_page = 50

    # 后台数据列表排序方式
    ordering = ('-create_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Recommend)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_url')
