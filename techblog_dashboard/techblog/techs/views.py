from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import csv
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.conf import settings
import os
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import plotly.express as px
import pandas as pd


##회원가입
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # 폼 저장
            return redirect('login')
        else:
            error_messages = form.errors.values()
            # 사용자에게 오류 메시지를 보여줌
            return render(request, 'techs/signup.html', {'form': form, 'error_messages': error_messages})
    else:
        print("POST 요청아님")
        form=SignUpForm()
    return render(request, 'techs/signup.html', {'form': form})


##로그인
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("로그인성공")
            return redirect('show_all')
        else:
            # 로그인 실패 처리
            return render(request, 'techs/login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'techs/login.html')

##로그아웃
def user_logout(request):
    logout(request)
    return redirect('show_all')


def show_all(request):
    islogin=False
    user_likes_instance=None
    like_list=[]
    print("화면진입")
    if request.user.is_authenticated:
        islogin=True
        username = request.user.username
        try:
            user_likes_instance = User_Likes.objects.filter(user__username=username)
            like_list=[like.post_id for like in user_likes_instance]
        except User_Likes.DoesNotExist and ObjectDoesNotExist: ##모두 False
            user_likes_instance = None

    posts = Post.objects.exclude(company=None).values(
        'pk','title', 'url', 'company__company_name', 'date', 'views', 'likes').order_by('-date')
    for p in posts:
        if islogin==False:
            p["was_liked"]="None"
        else:
            if p["pk"] in like_list:
                p["was_liked"]="True"
            else:
                p["was_liked"]="False"
        p["tag_list"]=[]
        tags=Post_tag.objects.select_related('tag').filter(post=p["pk"]).values('tag__tag_name')
        for tag in tags:
            p["tag_list"].append(tag)
    print(islogin)
    return render(request, 'techs/home.html', {"postings": posts, "islogin" : islogin})

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
    post_instance = Post.objects.get(id=Post_id)  # post_id에 해당하는 레코드 가져오기
    post_instance.likes += 1  # 'view' 필드 값 1 증가
    post_instance.save()  # 변경 사항 저장


    if request.user.is_authenticated:
        user_instance=User.objects.get(username=request.user.username)

        user_likes_instance, _=User_Likes.objects.get_or_create(
            user=user_instance,
            post=post_instance
            )
    else:
        print("ERROR")

    return redirect('show_all')


def get_all_file_names(directory_path):
    files = os.listdir(directory_path)
    file_names = [file for file in files if os.path.isfile(os.path.join(directory_path, file))]
    return file_names

def save_csv_to_model(request):
    all_files = get_all_file_names(settings.MEDIA_ROOT)
    for file_name in all_files:
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        now_company_name=file_name[:-4]

        with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #1. Company 테이블 저장 파일 목록 불러와서 -> 파일이름(회사명) 저장
            company_instance, _=Company.objects.get_or_create(company_name=now_company_name)

            for row in csv_reader:
                #2. Post 테이블 저장(각 csv 줄에 대하여)
                original_date_str = row['date']
                parsed_date = datetime.strptime(original_date_str, "%Y.%m.%d")
                iso_formatted_date = parsed_date.isoformat()
                post_instance, _=Post.objects.get_or_create(
                    title=row['title'],
                    company=company_instance,
                    date=iso_formatted_date,
                    url=row['link'],
                )

                # 3. Tag 테이블, post_tag 테이블 저장
                tags=row['tags'].split('#')
                for tag_name in tags:
                    #3-1. Tag 테이블 저장(Tag 테이블에 없는 태그에 대하여)
                    tag_instance, _ = Tag.objects.get_or_create(tag_name=tag_name)
                    
                    #3-2 Post_Tag 테이블 저장
                    Post_tag.objects.get_or_create(
                        post=post_instance,
                        tag=tag_instance,
                    )

                    company_tag, created = Company_Tag.objects.get_or_create(
                        company=company_instance,
                        tag=tag_instance,
                        defaults={'updates': datetime.now()}
                    )
                    
                    if not created:
                        company_tag.updates = datetime.now()
                        company_tag.count += 1
                        company_tag.save()
    return HttpResponse("CSV 파일을 처리했습니다.")

def all_chart(request):
    tag = pd.DataFrame.from_records(Post_tag.objects.all().values('tag__tag_name'))
    tag.drop(tag[tag['tag__tag_name'] == ''].index, inplace=True)
    tag_df = pd.DataFrame.from_records(Post_tag.objects.all().values('tag__tag_name').distinct())
    tag_df.drop(tag_df[tag_df['tag__tag_name'] == ''].index, inplace=True)
    count = pd.DataFrame(tag.groupby('tag__tag_name').size().reset_index(name='count'))
    top_20 = count.sort_values(by='count', ascending=False).head(20)
    all_df = pd.merge(tag_df, top_20, on='tag__tag_name')
    fig = px.bar(
        all_df, 
        x='count',
        y='tag__tag_name',
        title='Tag frequency in All posts',
        labels={'count':'Frequency', 'tag__tag_name':'Tags'},
        color='tag__tag_name'
    )
    fig.update_layout(
        height = 1000,
        yaxis={'categoryorder':'total ascending'},  # 빈도수가 높은 순으로 정렬
        yaxis_title='Tags',  # y축 제목 설정
        paper_bgcolor='#333', # 차트 바깥쪽 배경색
        plot_bgcolor='#333', # 차트 안쪽 배경색
        font = {'color':'white'},  # 전체 글자(폰트) 색상
    )

    plot_div = fig.to_json()

    print('Sending plot data...')
    return JsonResponse({'plot_div': plot_div})


def home(request):
    return render(request, 'home.html')

def company_chart(request, company):
    tag = pd.DataFrame.from_records(Company_Tag.objects.filter(company__company_name='{}'.format(company)).values('tag__tag_name'))
    count = pd.DataFrame.from_records(Company_Tag.objects.filter(company__company_name='{}'.format(company)).values('tag__tag_name', 'count'))
    company_df = pd.merge(tag, count, on='tag__tag_name')
    company_df.drop(company_df[company_df['tag__tag_name'] == ''].index, inplace=True)
    top_20 = company_df.sort_values(by='count', ascending=False).head(20)
    fig = px.bar(
        top_20,
        x='count',
        y='tag__tag_name',
        title='Tag frequency in {} posts'.format(company),
        labels={'count':'Frequency', 'tag__tag_name':'Tags'},
        color='tag__tag_name'
    )
    fig.update_layout(
        height = 1000,
        yaxis={'categoryorder':'total ascending'},  # 빈도수가 높은 순으로 정렬
        yaxis_title='Tags',  # y축 제목 설정
        paper_bgcolor='#333', # 차트 바깥쪽 배경색
        plot_bgcolor='#333', # 차트 안쪽 배경색
        font = {'color':'white'},  # 전체 글자(폰트) 색상
    )

    company_div = fig.to_json()

    print('Sending plot data...')
    return JsonResponse({'company_div': company_div})

