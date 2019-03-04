import logging
from django.shortcuts import render

# Create your views here.
from blog.models import Category

logger = logging.getLogger('blog.views')
from django.conf import settings


def global_setting(requst):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }


def index(request):
    category_list = Category.objects.all()

    return render(request, 'index.html', {'category_list': category_list})
