from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<int:pk>', views.viewPhoto, name='photo'),
    path('photo/add', views.addPhoto, name='add')
]
