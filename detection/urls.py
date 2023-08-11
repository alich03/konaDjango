# detection/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('test/', views.test1, name='upload_image'),
    path('pi/', views.process_image, name='upload_image'),

]
