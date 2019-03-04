from django.contrib import admin

# Register your models here.
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
            '/static/js/html5.js'
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
