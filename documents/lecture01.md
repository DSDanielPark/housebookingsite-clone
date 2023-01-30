# Airbnb lecture 1

## Requirements
1. python-peotry [설치](https://python-poetry.org/docs/) <br>
1.1 윈도우에서 <Br>
    
    ```
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```
    - 윈도우에서 설치 오류시, powershell 관리자 권한 실행 이후 `Set-ExecutionPolicy RemoteSigned`로 권한 변경
    ```
    pip install poetry
    ```

    1.2 Linux, MAC <br>

    ```
    brew install curl > brew install poetry
    ```
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    - 에러 발생시, 재설치 혹은 환경변수 체크

<Br>

2. 가상환경 셋팅

    ```
    peotry init
    peotry add django

    peotry shell #가상환경 실행
    django-admin
    exit #가상환경 종료

    peotry는 add가 install이다. ex peotry add beautifulsoup4
    ```

3. 나는 그냥 conda를 그대로.... conda가 윈도우에서 더 안정적임
    ```
    conda create -n airbnb python=3.8.5 
    conda activate airbnb
    pip install django
    ```

4. 장고 셋팅
    ```
    django-admin startproject config .
    ```

5. OOP
    - 장고도 파이썬도 객체 지향 프로그래밍(OOP)임.
        - Class
        - Inheritance
        - Method
        - Constructor: class 생성시 호출되는 함수   

6. 생성자 init 메서드의 self는 TypeScript나 JavaScript에서 사용하는 this랑 동일

    ```JavaScript
    //in java
    class Entrepreneur extends Player {
        constructor(
            firstName: string,
            lastName: string,
            private shares: number,
            private company: string
        ) {
            super(firstName, lastNAme)
        }
    }
    ```

    ```python
    #in python
    class Player:
        def __init__(self, name, xp):
            self.name = name
            self.xp = xp
    
    nico = palyer()
    ```


7. 상속 Inheritance

    ```python
    class Player:
        def __init__(self, name, xp):
            self.name = name
            self.xp = xp

        def say_hello(self):
            print(f'hello my name is {self.name}')

    class Fan:
        def __init__(self, name, fav_team):
            self.name = name
            self.fav_team = fav_team

         def say_hello(self):
            print(f'hello my name is {self.name}')
    ```

    - 위와 같이 say_hello 메서드가 중복사용되고 있으므로, 위에 Human 클래스에 say_hello를 생성해서 상속시켜주면 된다. 
    - 그러나 개인적으로 이건 맨 마지막에 이제 더이상 코드 리팩토링이나 래핑을 안한다고 가정할 경우에만 진행해야되는데, 왜냐하면 잘못된 상속과 이중 상속은 그 종속성을 풀어서 다시 싸야하는 매우 매우 고난과 역경의 시간을 겪어야 할 수 있으며, 정말 하나도 개발이 안끝나고 이러한 짓을 할 경우, 개발이 1개월 걸리면, 리팩토링이 3개월 걸릴 수 있으며 실제로 경험한 일이다.
    - 그래서 상속과 이중상속으로 정말 힘들게 짜여있으면, 그냥 몇가지 스니펫들만 꺼내와서 내가 다시 기능 구현하는게 파이썬의 경우 훨~씬 훨~씬 시간을 아낄 수 있다.

    ```python
    class Human:
        def __init__(self, name):
            self.name = name
            print("human init ok")

        def say_hello(self):
            print(f'hello my name is {self.name}')

    # 만약 Human의 파라미터를 전체로 사용하려면 super init해줘야함.

    class Player(Human):
        def __init__(self, name, xp):
            self.name = name #여기서는 player가 받은 이름이 노출되고
            self.xp = xp

    class Fan(Human):
        def __init__(self, name, fav_team):
            super().__init__(name) #여기도 Fan에 입력된 name이 입력되지만, 이게 Human클래스로 다시 들어가서 Human에 있는 init print가 출력됨
            self.fav_team = fav_team

    soccer_player = Player("SON", 32)
    soccer_player.say_hello()

    soccer_fan = Fan("Daniel", "Asnal")
    soccer_fan.say_hello()
    ```



    - 다른 예시

    ```python
    class Dog:
        def woof(self):
            print("ssssssssssssss")

    class Beagle(Dog):
        def jump(self):
            print("aaaaaaaaaaaaaaa")

    beagle = Beagle()
    beagle.woof()
    ### 아무일도 안일어남
    class Dog:
        def woof(self):
            print("ssssssssssssss")

    class Beagle(Dog):
        def jump(self):
            super().woof() #Dog.woof()
            print("aaaaaaaaaaaaaaa")

    beagle = Beagle()
    beagle.woof()
    ### parente class메서드 가 호출됨
    ```

    - 그리고 def __str__(self):도 있는데 이것도 나중에 사용
    - 자바와 마찬가지로, 파이썬의 모든 클래스는 기본적으로 최상위 클래스인 Object 클래스를 (보이지는 않지만) 상속함.
    - Object 클래스 안에는 여러 개의 __method__ 가 내장되어 있고 이는 기본적으로 정의되어 있는 메서드들임.
        - 당연히 우리가 만든 모든 클래스에도 사실 보이지는 않지만 저 메서드들이 정의가 되어있는 거죠(Object 클래스를 자동으로 상속받고 있으니까요) .
    - __str__() 메서드의 경우, 해당 클래스의 메모리 주소값을 반환합니다. 
        - 강의에서 한 것처럼, 이걸 오버라이딩해서 내 맘대로 바꿔 쓸 수 있습니다. 메모리 주소가 아니라 이모지를 반환하게 만든 것임.
    - 당연하게도 __str__()뿐 아니라, 필요하면 내장메서드 전부 맘대로 오버라이딩해서 바꿔 쓸 수 있음
    



<br>

8. __str__ 및 오버라이딩

    8.1 객체의 주소가 반환됨
    
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
        
    my_dog = Dog("nu_rung2")
    print(my_dog)

    friend_dog = Dog("hin_dung2")
    print(friend_dog) #계속 오버라이딩 됨
    
    ```


    8.2 객체가 ★로 오버라이딩 됨

    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return "★"
        
    my_dog = Dog("nu_rung2")
    print(my_dog)

    friend_dog = Dog("hin_dung2")
    print(friend_dog) #계속 오버라이딩 됨
    
    ```


    8.3 원하는대로 오버라이딩할 수 있음
    - 자체적으로 str을 리턴해주는 메서드가 print시에 실행된다고 보면 됨.


    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return f"Dog Name: {self.name}"
        
    my_dog = Dog("nu_rung2")
    print(my_dog)

    friend_dog = Dog("hin_dung2")
    print(friend_dog) #계속 오버라이딩 됨
        
    ```



    8.4 Dog이 어떤 클래스로부터 확장되고 있지 않아도, 우리 Dog 클래스는 파이썬 클래스의 객체이므로 그냥 super를 갖고 있음.


        ```python
        class Dog:
            def __init__(self, name):
                self.name = name
            def __str__(self):
                print(super().__str__())
                return f"Dog Name: {self.name}"
            
        my_dog = Dog("nu_rung2")
        print(my_dog)

        friend_dog = Dog("hin_dung2")
        print(friend_dog) #계속 오버라이딩 됨
        
        <__main__.Dog object at 0x000001B2C29D5988>
        Dog Name: nu_rung2
        <__main__.Dog object at 0x000001B2C29D5B08>
        Dog Name: hin_dung2

        print(dir(my_dog)) # 으로 클래스 내의 객체들을 확인할 수 있음.

        print(jia.name)
        ```


    <br>

    - 그래서 오버라이딩되기 전에 __str__을 호출하고, 그 다음에 오버라이딩 된 Dog Name 관련된 값을 리턴해주는 것을 볼 수 있음.
    <br>

    
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            print(super().__str__())
            return f"Dog Name: {self.name}"
        def __getattribute__(self, name):
            print(f'they want to get{name}')
            return "★"
    ```

    - 앞으로 dir로 볼 수 있는 property중에서 __str__을 주로 오버라이드해서 사용한다. 
    - classmethod들은 당연히 self를 첫번째 파라미터로 가져야만 한다.
        - 원칙적으로는 method의 parameter로 표현하지만, 실무에서는 대부분 argument로 통칭한다. 왜냐하면 딥러닝에서 업데이트되는 웨이트를 파라미터라고 주로 표현하기 때문이다. 파이썬은 거의 ai나 새로운 기능을 구현할 때 많이 사용되니까..
    - super() on the __init__에만 사용되는게 아니다. 그냥 parent class의 메서드를 호출하거나 할때 사용되지만 실무적으로 parent의 parameter를 상속받은 child class의 생성자에서 호출해줘야지 업데이트를 편하게 할 수 있기 때문에 주로 이중상속의 생성자는 child class의 생성자에서 호출되는게 흔할 뿐이다.

9. `gitignore` extension 설치하고, add gitignore하면 좋다. (없이 그냥 해도 된다.)