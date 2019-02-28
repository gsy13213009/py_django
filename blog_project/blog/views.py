import logging
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger('blog.views')
from django.conf import settings

def global_setting(requst):
    return {
        'SITE_NAME':settings.SITE_NAME,
        'SITE_DESC':settings.SITE_DESC,
    }

def index(request):
    try:
        open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())