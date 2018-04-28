# django-instagram
장고 인스타그램 clone coding project  
2018.2.27~2018.4.27
## 배포사이트
[http://lowell2735.pythonanywhere.com](http://lowell2735.pythonanywhere.com)
## 목표
- django,python 심층적으로 공부하기
- ajax 익히기
- 서툰 코드라도 스스로 해결하려고 노력하기
- 천천히 꾸준하게
## 로컬 환경 셋팅
1. virtualenv 생성 (python3.6 환경)
2. `pip install -r requirments.txt` 파이썬 패키지 설치
3. django_instagram/settings.py에서 SECRET_KEY,oauth KEY 설정
4. 파이썬 패키지 django/contrib/auth/urls.py 에서 app_name 추가
    ```python
    app_name = 'account'
    ```
5. `python manage.py migrate`  db 마이그레이션

## 서버 띄우기 
1. `python manage.py runserver` 실행

## 개발기
[http://jamanbbo.tistory.com/38](http://jamanbbo.tistory.com/38)