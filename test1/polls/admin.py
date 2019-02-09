from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # 两行，第一个为标题，后面为显示的内容
        ('hhhhh',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # 显示样式，显示三个信息
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加右侧的过滤器
    list_filter = ['pub_date']
    # 添加搜索框，搜索内容为question_text
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
