# Airbnb lecture 2

## 시작
한줄 요약
- `python manage.py migrate`
- `python manage.py runserver` 
- `python manage.py createsuperuser`
끝

<br>

1. 가상환경 시작
- `peotry shell` 혹은 conda로
- manage.py가 터미널에서 장고 실행
- 장고를 실제 서버에 배포할때는 다른 파이썬 파일 사용
- 개발 단계에서는 커맨드를 manage.py로 사용해서 이용

- `python manage.py runserver` - 장고 커맨드 터미널에서 실행
- 장고서버와 dev 서버도 실행됨


2. admin 
- http://127.0.0.1:8000/admin/

3. migratin - modify state of DB
- OperationalError at /adamin/에서의 첫 에러는 djanog_session이라는 DB 테이블을 찾았으나 실패한 것을 의미
- db.sqlite3가 DB파일인데 admin user를 위한 session을 만드려고 했는데 django_session을 찾지 못했다는 에러
- Django는 이미 DB의 state를 변경할 수 있는 파이썬 코드를 가지고 있음. (18개)
- Django는 18개의 migration 파일을 갖고 있음 -> DB state 수정
- 장고는 세션, 패스워드 등 모든 유저 데이터를 DB에 저장
- `migration file: DB의 모양은 transfomation 시키는 python code`

4. 정리
- `python manage.py migrate` >> 18개의 파일에 아직 DB에 적용되지 않은 transfomation이 있음
- `python manage.py runserver` 
- http://127.0.0.1:8000/admin/

5. admin user 생성
- `python manage.py createsuperuser`
- 비밀번호 해싱이나 생성, 관리 등등 매우 편하게 한번에 끝

6. tip
- "CSRF_TRUSTED_ORIGINS(403)" 에러 뜨는 분들은 `config/settings.py`에 다음과 같이 입력

`CSRF_TRUSTED_ORIGINS=['https://*.[사이트도메인]']`

<br>
<Br>

### Library와 Framework 차이
1. request로 이해하기
- 웹사이트에 요청 보내려면 requests 사용함
- library의 경우, 개발자가 import library한다음에 call하는 것
- FrameWork는 개발자의 코드를 call함 -> 개발자의 코드를 보고, 그곳에 정합성에 부합하는 코드가 있으면 그 코드를 사용함 -> 즉 개발자가 Framwork를 호출하는게 아니라 Framework가 제대로 오버라이딩 되어 있는 개발자의 코드가 있으면 그 코드를 호출해서 업데이트하는 것 정도의 차이 -> 대부분 인터페이스에 맞게 뭔가를 오버로딩되게 되어있는 것들이랑 비슷(블록체인에서 대부분 그랬음)
- 예시 

    ```
    setting.py의 변수를 다음과 같이 바뀌면 서버 재시작되면서, local time이 바뀌는데 이처럼 프레임워크는 이미 짜여진 구조에 변수를 변경하거나 특정 인터페이스에 맞게 개발을 하면 그것을 호출함
    TIME_ZONE = "Asia/Seoul"
    ```
- 

### Concept of Application in django
- 예를 들어 방검색과 유저에 대한 로직의 경우 DB에 분리하는데 이럴 경우 2개의 application이라고 볼 수 있음. 
- django app은 애플리케이션 로직과 데이터를 합쳐서 encapsulation함.
- review도 또 다른 로직과 다른 폴더와 파일이 돌아야되니까 또 다른 application이라고 볼 수 있음.
- 각 application마다 접근은 가능하지만, 분리되어 있어야 편함