from django.urls import path
from . import views


urlpatterns = [
    path('learning_logs_2/', views.index_2)
]
