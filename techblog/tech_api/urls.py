from django.urls import path, include
from .views import *
from . import views




#Generapiview 때문에 <int:id>에서 pk로 수정해줘야함
urlpatterns = [
    path('post/', PostList.as_view(), name='post-list'),
]