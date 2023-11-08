from rest_framework import serializers
from techs.models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password




class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'company', 'date','views', 'likes','url']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','tag_name']    

class Post_tagserializer(serializers.ModelSerializer):
    class Meta:
        model = Post_tag
        fields = ['id', 'post', 'tag']

class Compnay_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Tag
        fields = ['id', 'company', 'tag','count', 'updates']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'company_name']