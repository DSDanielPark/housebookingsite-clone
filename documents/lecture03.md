# Airbnb lecture 2

## House application 생성

1. startapp
- `python manage.py startapp houses`
- 나중에는 uses app이나 뭐 다양한 app을 할때도 동일
- `houses` 폴더 생기고 여기에 models.py에 db 모양은 설명함.

2. config 추가
- config/setting.py에 다음과 같이 houses 앱을 추가하고

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "houses.apps.HousesConfig"
]

- 혹은 CUSTOM_APPS = ["houses.apps.HousesConfig"], SYSTEMP_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles"]
    한다음에
    - INSTALLED_APPS = CUSTOM_APPS + SYSTEMP_APPS로 해도됨
    - 프레임워크니까 필수 요소나 VARIABLE들만 포맷에 맞게 정의해주면 됨


3. model 정의
- houses\models.py에 다음과 같이 House 모델에 대해서 정의한다음에
    - SQL쓰지 않고 다음과 같이 DB구조 정의

    ```
    class House(models.Model):
        '''houses model'''
        name = models.CharField(max_length=100)
        price = models.PositiveBigIntegerField()
        description = models.TextField()
        address = models.CharField(max_length=140)
    ```

4. admin 정의

    ```
    # House Admin이 House 클래스를 관리하도록 데코레이팅 되어 있음
    # 즉 House 모델에 admin을 생성할건데, admin.ModelAdmin을 그대로 상속받아서
    # 구조체를 사용할거다정도의 의미 재미나게 짜놨네
    @admin.register(House)
    class HouseAdmin(admin.ModelAdmin):

        pass
```


5. 3번 model에 정의한 구조 변경
- 변경하고, python manage.py makemigrations하면 다음 경로에 저절로 구조체 생성
- houses\migrations
- 그리고 정상적으로 잘 확인되면 python manage.py migrate로 마이그레이트하면 됨 -> DB와 장고 연결 

