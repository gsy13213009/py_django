from django.db import models

# Create your models here.
class DownloadInfo(models.Model):
    client_timestamp = models.CharField(max_length=15, default='', null=True)
    sdk_version_code = models.CharField(max_length=10, default='', null=True)
    event_source = models.CharField(max_length=50, default='', null=True)
    event_id = models.CharField(max_length=50, default='', null=True)
    event_type = models.CharField(max_length=50, default='', null=True)
    download_url = models.CharField(max_length=500, default='', null=True)
    apk_package_name = models.CharField(max_length=50, default='', null=True)
    apk_version_code = models.CharField(max_length=10, default='', null=True)
    apk_size = models.CharField(max_length=10, default='', null=True)
    progress = models.CharField(max_length=5, default='', null=True)
    ad_join_id = models.CharField(max_length=20, default='', null=True)
    app_id = models.CharField(max_length=50, default='', null=True)
    h5_extra_data = models.CharField(max_length=100, default='', null=True)
    pause_cause = models.CharField(max_length=20, default='', null=True)
    state = models.CharField(max_length=10, default='', null=True)
    dp_extension = models.CharField(max_length=50, default='', null=True)
    image_url = models.CharField(max_length=100, default='', null=True)
    type = models.CharField(max_length=10, default='', null=True)
    pub_date = models.DateTimeField()
    cfm_download = models.CharField(max_length=2, default='', null=True)
