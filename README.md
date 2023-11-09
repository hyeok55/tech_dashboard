# DEV Project1
Techblog를 크롤링하여 시각화 및 대시보드 구축 웹 프로젝트

------------

#Demo video
[![SeeNear](https://user-images.githubusercontent.com/54880474/229173623-2b5241ae-dc6c-488f-8b63-a9108537ed76.jpg)](https://youtu.be/eu4VRWWW2r4)  

------------

# 목차
- [개발 환경](#개발-환경)
- [역할](#역할)
- [사용 기술](#사용-기술)
    * [백엔드](#백엔드)
    * [프론트엔드](#프론트엔드)
    * [Github Rule](#github-rule)
- [핵심 키워드](#핵심-키워드)
- [E-R 다이어그램](#e-r-다이어그램)
- [프로젝트 목적](#프로젝트-목적)
- [핵심 기능](#핵심-기능)

------------

## 개발 환경
- GitHub
- Mysql Workbench
- Visual Studio Code

## 역할
### Crawling & preprocessing

- 박진영 : 크롤링(6개 사이트) 및 태그 전처리
- 이보경 : 크롤링(5개 사이트)
- 김바롬 : 크롤링(6개 사이트)

### Visualization

- 김바롬(전체 태그 빈도수 & 기업별 태그 빈도수)

### Web(Django)

- 프론트엔드
    - 게시글 (김혁)
    - 시각화 (이보경)
- 백엔드
    - 메인페이지 (김혁,최은서)
    - API 구상 (김혁,최은서)
    - 조회 (김혁,최은서)
    - 테스트 코드 작성 (김혁,최은서)
    - DB 구축 및 연동 (최은서)

## 사용 기술
### 백엔드
#### 주요 프레임워크 / 라이브러리
- Python3
- Django
- SpringBoot Security
- Bs4

#### Database
- Mysql

### 프론트엔드
- Javascript
- Html/Css

### Github Rule
#### Commit Message rule

1. 제목과 본문을 한 줄 띄어 구분
2. 제목은 50자 이내
3. 제목 첫 글자는 대문자
4. 제목 끝에 마침표 X
5. 제목은 명령문으로, 과거형 X
6. 본문의 각 행은 72자 이내 (줄바꿈 사용)
7. 본문은 어떻게 보다 무엇을, 왜에 대하여 설명

#### Branch naming

- 어떤 이름도 가능하다. 단, `master`, `develop`, `release-...`, `hotfix-...` 같은 이름은 사용할 수 없다.
- `feature/기능요약` 형식을 추천한다. ex) feature/login

#### Pull & Request Rule

- main branch로 바로 push 했을 경우 error 발생
- 따로 Branch를 만들어 PR을 날리도록 함
- **administrator만 merge가 가능함**
- 강제로 **코드리뷰**를 의무화함
- 무분별한 Merge, Push를 방지

#### pull&request 보낼때

- 이름 + 기능 적기!

#### pull&request 받을 때

- approve review 1명 이상일 시 merge

#### Merge

- 관리자 승인

## 핵심 키워드

- bs4, selenium을 통한 Web Scrapping
- Django를 통한 백엔드 서버 개발
- Django Form을 이용한 프론트 개발

## E-R 다이어그램
![image](https://velog.velcdn.com/images/jg31109/post/4e6cfb5f-51ff-4671-8fa6-ec52b26ffe63/image.png)

### Post_tag, company_tag가 있어야 하는 이유

1. post테이블만 있으면 되는데 왜 company_tag, tag, company 테이블을 추가했는가
데이터 시각화 시 정보를 빠르게 불러오기 위해서(기존의 post 테이블에서 정보를 조회할 경우 select from where 구문을 이용해서 불러와야 하기 때문에 데이터가 많아지면 시간이 오래 걸리는 이슈가 발생한다)
2. post_tag 테이블 생성 이유(데이터 일관성 이슈)
post 테이블과 tag 테이블은 N:M 관계이므로 CRUD시 데이터 일관성이 유지되지 못할 확률이 크다. 따라서 N:1, 1:M 관계로 만들어 하나의 테이블에서만 CRUD가 일어나도록 한다.



## 프로젝트 목적

### 해당 프로젝트를 기획한 이유? 

모든 프로젝트는 User에게 필요한 서비스여야하고 설득력이 있어야 된다고 생각했습니다.
"우리 팀에게 필요한 서비스를 만들자" 에서 시작하여, 저희가 자주 참고하는 Tech를 기술하는 블로그의 내용을 크롤링해서 
블로그 태그별 시각화 및 블로그 접근성을 높일 수 있는 대시보드를 제작하자는 아이디어를 확립했습니다.

## 핵심 기능


### 20개의 기업의 테크 블로그 리스트화 및 URL 연결 제공
### 기업별 태그 시각화
### 테크블로그 검색 및 조회







