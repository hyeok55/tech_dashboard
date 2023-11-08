from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all, name='show_all'),
    path('search/<str:query>', views.searchquery, name='searchquery'),
    path('updateview/<int:Post_id>/', views.increaseviews, name='increaseview'),
    path('updatelike/<int:Post_id>/', views.increaselikes, name='increaselikes'),
]
