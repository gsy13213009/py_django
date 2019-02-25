from django.db import models

# Create your models here.
class DownloadInfo():
    client_timestamp = models.CharField(max_length=15)
    sdk_version_code = models.CharField(max_length=10)
    download_url = models.CharField(max_length=500)
    apk_package_name = models.CharField(max_length=50)
    apk_version_code = models.CharField(max_length=10)
    apk_size = models.CharField(max_length=10)
    appid = models.CharField(max_length=50)
    ad_join_id = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    h5_extra_data = models.CharField(max_length=100)
    pause_cause = models.CharField(max_length=20)
    progress = models.CharField(max_length=5)
    state = models.CharField(max_length=10)
    dp_extension = models.CharField(max_length=50)
    imageurl = models.CharField(max_length=100)
    type = models.CharField(max_length=10)