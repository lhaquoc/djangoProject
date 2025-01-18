from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^departments$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),
]
