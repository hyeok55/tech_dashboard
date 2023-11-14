# DEV Project1
<img src="https://velog.velcdn.com/images/jg31109/post/2eeba08f-7437-46af-8ce5-e7e2ebae25ca/image.png" width="200" height="200"/>
Techblog를 크롤링하여 시각화 및 대시보드 구축 웹 프로젝트

------------

# Demo video
[Demo video](https://www.canva.com/design/DAFzszeqXbI/AupPsP-IXNDfOIGxVlGINg/watch?utm_content=D[…]re_your_design&utm_medium=link&utm_source=shareyourdesignpanel)
![Demo GIF](readme/1-2팀 Demo_video.gif)

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
    - 게시글 (최은서)
    - 시각화 (이보경)
- 백엔드
    - 메인페이지 (김혁,최은서)
    - API 구상 (김혁,최은서)
    - 조회 (김혁,최은서)
    - 테스트 코드 작성 (김혁,최은서)
    - DB 구축 및 연동 (김혁,최은서)
    - 회원가입/로그인 (최은서)

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
![image](https://github.com/hyeok55/tech_dashboard/assets/77157003/7f86280b-7908-494b-b31e-5c5a7c7e3984)


## 프로젝트 목적

### 해당 프로젝트를 기획한 이유? 

모든 프로젝트는 User에게 필요한 서비스여야하고 설득력이 있어야 된다고 생각했습니다.
"우리 팀에게 필요한 서비스를 만들자" 에서 시작하여, 저희가 자주 참고하는 Tech를 기술하는 블로그의 내용을 크롤링해서 
블로그 태그별 시각화 및 블로그 접근성을 높일 수 있는 대시보드를 제작하자는 아이디어를 확립했습니다.

## 핵심 기능


### 20개의 기업의 테크 블로그 리스트화 및 URL 연결 제공
### 기업별 태그 시각화
### 테크블로그 검색 및 조회







