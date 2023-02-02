from django.contrib import admin
from .models import House

# Register your models here.


# House Admin이 House 클래스를 관리하도록 데코레이팅 되어 있음
# 즉 House 모델에 admin을 생성할건데, admin.ModelAdmin을 그대로 상속받아서
# 구조체를 사용할거다정도의 의미 재미나게 짜놨네
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    pass