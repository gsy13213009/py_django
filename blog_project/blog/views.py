import logging

from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import render

# Create your views here.
from blog.models import Category, Article

logger = logging.getLogger('blog.views')
from django.conf import settings


def global_setting(requst):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }


def index(request):
    category_list = Category.objects.all()
    # 获取所有的文章数量
    article_list = Article.objects.all()
    # 初始化分页器Paginator
    paginator = Paginator(article_list, 2)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except:
        article_list = paginator.page(1)
    try:
        # 文章归档，先获取文章中的 年-月
        # print(Article.objects.values('date_publish').distinct())

        #  第一种执行sql的方式

        # 因为一个%代表占位，所以使用%%，第一个把第二个转义一下
        # archive_list = Article.objects.raw('SELECT DISTINCT id, date_publish, DATE_FORMAT(date_publish, "%%Y-%%m") as col_date FROM blog_article ORDER BY date_publish')
        # for archive in archive_list:
        #     print(archive)

        # 第二种方式，使用connection去执行数据库代码

        # cursor = connection.cursor()
        # cursor.execute('SELECT DISTINCT id, date_publish, DATE_FORMAT(date_publish, "%%Y-%%m") as col_date FROM blog_article ORDER BY date_publish')
        # row = cursor.fetchall()
        # print(row)
        print(Article.objects.distinct_date())

    except Exception as e:
        print(e)
    return render(request, 'index.html', locals())
