from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from download_info.models import DownloadInfo
import json


def index(request):
    return render(request, './download_info/index.html')

def report(request):
    download_info = DownloadInfo()

    download_info.client_timestamp = request.POST.get('client_timestamp')
    download_info.sdk_version_code = request.POST.get('sdk_version_code')
    download_info.download_url = request.POST.get('download_url')
    download_info.apk_package_name = request.POST.get('apk_package_name')
    download_info.apk_version_code = request.POST.get('apk_version_code')
    download_info.apk_size = request.POST.get('apk_size')
    download_info.app_id = request.POST.get('app_id')
    download_info.ad_join_id = request.POST.get('ad_join_id')
    download_info.ld = request.POST.get('ld')
    download_info.h5_extra_data = request.POST.get('h5_extra_data')
    download_info.pause_cause = request.POST.get('pause_cause')
    download_info.progress = request.POST.get('progress')
    download_info.state = request.POST.get('state')
    download_info.dp_extension = request.POST.get('dp_extension')
    download_info.image_url = request.POST.get('image_url')
    download_info.type = request.POST.get('type')
    download_info.pub_date = timezone.now()

    if download_info.client_timestamp is not None:
        download_info.save()
        resp = {'code':0, 'detail':'ok , report success'}
    else:
        resp = {'code': -1, 'detail':'fail , report fail'}

    return HttpResponse(json.dumps(resp), content_type='application/json')