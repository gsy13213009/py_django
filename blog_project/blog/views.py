import logging

from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Count
from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import CommentForm
from blog.models import Category, Article, Comment

logger = logging.getLogger('blog.views')
from django.conf import settings


def global_setting(requst):
    SITE_URL = settings.SITE_URL
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    category_list = Category.objects.all()
    archive_list = Article.objects.distinct_date()
    # 标签云
    # 广告
    # 友情链接
    # 浏览排行
    article_click_list = Article.objects.all().order_by('-click_count')[:6]
    # 评论排行
    # 1. 分别取出所有comment里的article字段，然后做个聚合Count函数，命名为comment_count，然后排序
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]

    # 站长推荐
    article_recommend_list = Article.objects.filter(is_recommend=False)[:6]
    return locals()


def index(request):
    # 获取所有的文章数量
    article_list = get_page_list(request, Article.objects.all())
    return render(request, 'index.html', locals())


def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)

    # 获取文章数量
    article_list = Article.objects.filter(date_publish__icontains=year + '-' + month)
    # 初始化分页器Paginator
    article_list = get_page_list(request, article_list)

    return render(request, 'archive.html', locals())


def article(request):
    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist as e:
        print(e)
        logger.error(e)
        return render(request, 'failure.html', {"reason": "没有找到文章"})
    # 评论表单
    comment_form = CommentForm({
                                   'author': request.user.username,
                                   'email': request.user.email,
                                   'url': request.user.url,
                                   'article': id
                               })
    return render(request, 'article.html', locals())

def comment_post(request):
    try:
        comment_info = CommentForm(request.POST)
        if comment_info.is_valid():
            comment = Comment.objects.create(
                user_name=comment_info.cleaned_data['author'],
                email=comment_info.cleaned_data['email'],
                url=comment_info.cleaned_data['url'],
                content=comment_info.cleaned_data['comment'],
                article=comment_info.cleaned_data['article'],
                user=request.user if request.user.is_authenticated() else None
            )
            comment.save()
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])


def get_page_list(request, list):
    paginator = Paginator(list, 2)
    try:
        page = request.GET.get('page', 1)
        list = paginator.page(page)
    except:
        list = paginator.page(1)
    return list
