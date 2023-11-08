from django.shortcuts import render
from rest_framework import generics, permissions
from techs.models import *
from tech_api.serializers import *

# Create your views here.



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
