# HTML

# 목차
1. 장고 프로젝트 생성
  - DB 설정
2. MVC 와 MTV 
3. Django 개발환경 
4. 게시판 앱 만들기
  - URL → VIEW → template

# 장고 프로젝트 생성
1. django 명령어를 활용해 project 생성
```bash
django-admin startproject config .
```

2. 폴더가 하나 생성되고, 하위 폴더로는 config 폴더가 생성된다. 

3. 생성된 폴더에 접근하여 다음과 같은 명령어를 입력하여 localhost:8000 을 입력해준다. 
```bash
python manage.py runserver
```
## DB 설정
django는 모델로 데이터 관리가 가능하다. SQL을 사용하지 않고도 모델만으로 데이터를 저장, 조회를 관리할 수 있는데, `migrate` 명령어로 앱들이 필요로 하는 테이블을 생성해줄 수 있다.
```bash
python manage.py migrate
```

이후, 관리자 페이지에 접근할 수 있도록 아이디와 비밀번호를 생성시켜준다. 비밀번호 입력시 영문과 숫자를 섞고 최소 8자리로 해야한다. 
```bash
python manage.py createsuperuser

Username (leave blank to '~') : admin
Email address : abc@gmail.com
Password :
Password (again) :
Suyperuser created successfully
```

# MVC와 MTV
- MVC (Model - View - Controller): Web 프로그래밍에서 자주 사용되는 디자인 패턴
- MTV (Model - Template - View) :  장고 이자인 패턴
  
## 파이썬 스크립트 종류 
- models.py : DB 관리
- admin.py : 기본관리자 페이지 사용
- views.py : DB를 가지고와서 HTML에 구현할 페이지를 맡는 곳
- urls.py : url 설정
- templates : html이 있는 곳 
- config/settings.py 

# Django 개발환경
## config 폴더
- urls.py :한 프로젝트에 안에 여러개의 urls 파일을 만들어지는데, 각 urls파일의 기준이 되는 url을 설정하는 곳
- wsgi.py : 웹 서비스를 실행하기 위한 wsgi 관련 내용이 있음
- settings.py : 프로젝트 설정에 관한 내용 포함

|이름|기능|
|---|---|
|BASE_DIR| 프로젝트 루트 폴더 |
|SECRET_KEY| 다양한 보안을 위해 사용|
|DEBUG| 디버그 모드 설정, TRUE일 경우 오류 메시지 확인 가능(ex. 404), 실제 배포시 false 변경  |
|ALLOWED_HOSTS| 현재 서비스의 호스트 설정. 배포시 실제 도메인을 기록 |
|<b>INSTALLED_APPS</b>|장고는 다양한 앱의 결합으로 만들어지기 때문에, 현재 프로젝트에서 사용하는 앱의 목록을 기록하고 관리|
|<b>ROOT_URLCONF</b>|기준이 되는 urls.py파일의 경로설정|
|<b>TEMPLATES</b>|장고에서 사용되는 템플릿(html, css) 시스템 설정|
|DATABASE|DB설정|
|LANGUAGE_CODE|다국어에 관한 설정|

- db.sqlite3 : SQLite DB를 사용할 경우 임의로 삭제하거나 위치이동 금지 다른 DB로 변경하는 경우 필요없는 파일
- manage.py : 장고의 다양한 명령어를 실행하기 위한 파일

# 게시판 앱 만들기
PDF 파일 참고