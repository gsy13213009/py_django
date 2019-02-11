
from django.conf.urls import url

from . import views

urlpatterns = [
    url('register/', views.register),
    url('register_handle/', views.register_handle),
]