from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path("archive/", views.archive, name='archive'),
    path("article/", views.article, name='article'),
]