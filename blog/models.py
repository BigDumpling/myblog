
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Constant(models.Model):
    status = models.IntegerField(default=1)
    param_key = models.CharField(max_length=32)
    param_name = models.CharField(max_length=64)
    param_value = models.CharField(max_length=256)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 't_constant'
        verbose_name = '配置常量'
        verbose_name_plural = '配置常量'

    def __str__(self):
        return self.param_name


class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')
    status = models.IntegerField(default=1)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 't_category'
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)
    status = models.IntegerField(default=1)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 't_tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Recommend(models.Model):
    name = models.CharField('推荐位', max_length=100)
    status = models.IntegerField(default=1)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 't_recommend'
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    status = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('阅读量', default=0)
    recommend = models.ForeignKey(Recommend, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    modify_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 't_article'
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    status = models.IntegerField(default=1)
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.text_info

    class Meta:
        db_table = 't_banner'
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)
    status = models.IntegerField(default=1)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_link'
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
