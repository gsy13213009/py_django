import logging
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger('blog.views')

def index(request):
    try:
        open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())