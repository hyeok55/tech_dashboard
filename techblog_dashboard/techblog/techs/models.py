from django.db import models
from django.contrib.auth.models import User

like_list=[]

class Company(models.Model):
    company_name = models.CharField(max_length=30, verbose_name='회사명', unique=True)

    def __str__(self):
        return f'{self.company_name}'


class Post(models.Model):
    # post_id  pk
    title = models.CharField(max_length=200, verbose_name='제목')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='회사')
    date = models.DateTimeField(verbose_name='작성일')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    url = models.TextField(verbose_name='링크', unique=True)

    def __str__(self):
        return f'{self.title},{self.company.company_name},{self.date},{self.views},{self.likes}'


class Tag(models.Model):
    # tag_id pk
    tag_name = models.CharField(max_length=200, verbose_name='태그 내용', unique=True)

    def __str__(self):
        return f'{self.tag_name}'


class Post_tag(models.Model):
    # post_tag_id pk
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='게시글')  # class Post
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            verbose_name='태그')  # class Tag

    def __str__(self):
        return f'{self.post.title},{self.tag.tag_name}'


class Company_Tag(models.Model):
    # company_tag_id pk
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='회사')  # class Post
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            verbose_name='태그 내용')  # class Post# tag table
    count = models.IntegerField(default=0)
    updates = models.DateTimeField(verbose_name='업데이트 날짜', auto_now=True)

    def __str__(self):
        return f'{self.company.company_name},{self.tag.tag_name}'


# class User(models.Model): 내장된 User 모델이다.
#     # user_id 
#     user_email=models.CharField(max_length=50, verbose_name='이메일주소')
#     user_password=models.CharField(max_length=20, verbose_name='패스워드')

#     def __str__(self):
#         return f'{self.user_email},{self.user_password}'

class User_Likes(models.Model):
    # user_likes_id  pk
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,
                            verbose_name='사용자')  # class Post# tag table
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE,
                            verbose_name='게시글')  # class Post# tag table

    def __str__(self):
        return f'{self.user_id.username},{self.post_id.title}'