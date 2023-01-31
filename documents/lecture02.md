# Airbnb lecture 2

## 시작
1. 가상환경 시작
- `peotry shell` 혹은 conda로
- manage.py가 터미널에서 장고 실행
- 장고를 실제 서버에 배포할때는 다른 파이썬 파일 사용
- 개발 단계에서는 커맨드를 manage.py로 사용해서 이용

- `python manage.py runserver`
- 장고서버와 dev 서버도 실행됨

- http://127.0.0.1:8000/admin/

- OperationalError at /adamin/에서의 첫 에러는 djanog_session이라는 DB 테이블을 찾았으나 실패한 것을 의미
- db.sqlite3가 DB파일인데 admin user를 위한 session을 만드려고 했는데 못 찾은 것 -> 이런 테이블 생성 migration