import logging

from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import render

# Create your views here.
from blog.models import Category, Article

logger = logging.getLogger('blog.views')
from django.conf import settings


def global_setting(requst):
    category_list = Category.objects.all()
    archive_list = Article.objects.distinct_date()
    # 标签云
    # 广告
    # 友情链接

    return {
        'category_list': category_list,
        'archive_list': archive_list,
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }


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


def get_page_list(request, list):
    paginator = Paginator(list, 2)
    try:
        page = request.GET.get('page', 1)
        list = paginator.page(page)
    except:
        list = paginator.page(1)
    return list
