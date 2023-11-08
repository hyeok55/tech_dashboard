from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200, verbose_name = '회사명')

    def __str__(self):
        return f'{self.company_name}'

class Post(models.Model):
    #post_id  pk
    title = models.CharField(max_length=200, verbose_name = '제목')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,verbose_name='회사')
    date = models.DateTimeField(verbose_name = '작성일')
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    url = models.URLField(max_length=200,verbose_name = '링크')

    def __str__(self):
        return f'{self.title},{self.company.company_name},{self.date},{self.views},{self.likes}'


class Tag(models.Model):
    # tag_id pk
    tag_name = models.CharField(max_length=200, verbose_name = '태그 내용')

    def __str__(self):
        return f'{self.tag_name}'


class Post_tag(models.Model):
    # post_tag_id pk
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글') #class Post
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,verbose_name='태그') # class Tag

    def __str__(self):
        return f'{self.post.title},{self.tag.tag_name}'
    


class Company_Tag(models.Model):
    #company_tag_id pk
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='회사') #class Post
    tag  = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='태그 내용') #class Post# tag table
    count = models.IntegerField(default = 0)
    updates = models.DateTimeField(verbose_name = '업데이트 날짜')

    def __str__(self):
        return f'{self.company.company_name},{self.tag.tag_name}'

