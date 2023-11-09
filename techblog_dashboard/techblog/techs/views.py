from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .visualization import *
import csv

def read_csv(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        return list(map(int, list(reader)[1]))

def write_csv(now_list, file_name):
    fields=['pk']
    rows=[list(set(now_list))]
    with open(file_name, 'w', newline='') as f:
        write = csv.writer(f) 
        write.writerow(fields) 
        write.writerows(rows)

like_list = read_csv("../liked.csv")

def show_all(request):
    posts = Post.objects.exclude(company=None).values(
        'pk','title', 'url', 'company__company_name', 'date', 'views', 'likes').order_by('-date')
    for p in posts:
        if p["pk"] in like_list:
            p["was_liked"]="True"
        else:
            p["was_liked"]="False"
        p["tag_list"]=[]
        tags=Post_tag.objects.select_related('tag').filter(post=p["pk"]).values('tag__tag_name')
        for tag in tags:
            p["tag_list"].append(tag)
        print(p["pk"])
        print(like_list)
    print(posts)

    return render(request, 'techs/home.html', {"postings": posts})

def searchquery(request, query):
    company_list=[]
    tag_list=[]
    companies=list(Company.objects.values('company_name'))
    for company in companies:
        company_list.append(company["company_name"])
    tags=list(Tag.objects.values('tag_name'))
    for tag in tags:
        tag_list.append(tag["tag_name"])
    if query in company_list:
        posts = Post.objects.exclude(company=None).values('pk','title', 'url', 'company__company_name', 'date', 'views', 'likes').filter(company__company_name=query).order_by('-date')
        for p in posts:
            if p["pk"] in like_list:
                p["was_liked"]="True"
            else:
                p["was_liked"]="False"
            p["tag_list"]=[]
            tags=Post_tag.objects.select_related('tag').filter(post=p["pk"]).values('tag__tag_name')
            for tag in tags:
                p["tag_list"].append(tag)
        return render(request, 'techs/home.html', {"postings": posts})
    elif query in tag_list:
        posts = Post.objects.exclude(company=None).values(
        'pk','title', 'url', 'company__company_name', 'date', 'views', 'likes').order_by('-date')
        for p in posts:
            if p["pk"] in like_list:
                p["was_liked"]="True"
            else:
                p["was_liked"]="False"
            p["tag_list"]=[]
            tags=Post_tag.objects.select_related('tag').filter(post=p["pk"]).filter(tag__tag_name=query).values('tag__tag_name')
            for tag in tags:
                p["tag_list"].append(tag)
        return render(request, 'techs/home.html', {"postings": posts})
    else:
        posts = Post.objects.none()
        return render(request, 'techs/home.html', {"postings": posts})

def increaseviews(request, Post_id):
    post = Post.objects.get(id=Post_id)  # post_id에 해당하는 레코드 가져오기
    post.views += 1  # 'view' 필드 값 1 증가
    post.save()  # 변경 사항 저장
    return redirect('show_all')

def increaselikes(request, Post_id):
    like_list.append(Post_id)
    write_csv(like_list, "../liked.csv")
    post = Post.objects.get(id=Post_id)  # post_id에 해당하는 레코드 가져오기
    post.likes += 1  # 'view' 필드 값 1 증가
    post.save()  # 변경 사항 저장
    return redirect('show_all')


def all_chart(request):
    all_tags()
    return render(request, 'techs/home.html')

def company_chart(request, company):
    company_tags(company)
    return render(request, 'techs/home.html')

def company_name(request):
    select_company = Company.objects.values_list('company_name', flat=True).distinct()
    return render(request, 'techs/home.html', {'select_company': select_company})