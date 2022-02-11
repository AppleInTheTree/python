#chapter06_01
#CLASS
#OOP, self, instance method, instance variable

#클래스 and 인스턴스 차이 이해
#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
#클래스 변수 : 직접 접근 가능, 공유 
#인스턴스 변수 : 객체마다 별도 존재
#ex1)

from telnetlib import SE
from this import d


class dog: #object 상송
    #클래스 속성
    species = 'fisrtdog'

    #초기화/인스턴스 속성

    def __init__(self, name, age):
        self.name = name
        self.age = age

#클래스 정보
print(dog)

#인스턴스화
a = dog("ralf", 2)
b = dog("micky", 4)

#네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name,a.age, b.name, b.age))

if a.species == 'fisrtdog':
    print('{} is {}'.format(a.name, a.species))

print(dog.species)
print(a.species)

#ex2
# self의 이해 
#self를 붙이면 인스턴스 메소드가 된다. 
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self): #인스턴스 메소드 , self가 붙으면 인스턴스 메소드가 된다.
        print('Func2 called')

f = SelfTest()

SelfTest.func1()#클래스 메소드
f.func2()#인스턴스 메소스

#ex3)
#클래스는 공용 인스턴스는 나만의

class wareHouse:
    #클래스변수
    stock_num = 0 # 재고

    def __init__(self, name): #생성자 시작할때 만들어진다. 
        self.name = name
        wareHouse.stock_num += 1
        
    def __del__(self): # 소멸자 
        wareHouse.stock_num -= 1

user1 = wareHouse('Lee')
user2 = wareHouse('Ahn')

print(wareHouse.stock_num)

del user1

print(wareHouse.__dict__)

#예제4)
class dog2: #object 상송
    #클래스 속성
    species = 'fisrtdog'

    #초기화/인스턴스 속성

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} tears old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {} !".format(self.name, sound)


#인스턴스 생성 

c = dog2('july', 4)
d = dog2('Marrt', 10)
#메소드 호출 
print(c.info())
print(c.speak("hi"))
# 하나의 클래스를 잘 만들면 여러가지의 것들을 표현할 수 있다. 