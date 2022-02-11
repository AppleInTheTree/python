#chapter05_01
#파이션 함수 및 중요성
#파이썬 함수식 및 람다

#함수 정의 방법
#def function_name(parameter):
#   code

#ex1)

from tkinter import Y


def first_func(w):
    print('Hello,', w)

word = "goodboy"

first_func(word)

#예제2
def return_func(w1):
    value = "Hello ," + str(w1)
    return value

x =return_func('Goodboy2')
print(x)

#예제3(다중반한)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3=  x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x,y,z)

#예제4 모든 자료형으로 형태만 만들면 리턴 가능

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3=  x * 30
    return (y1, y2, y3)

x = func_mul(10)

print(type(x), list(x))

# 중요
# *args, **kwargs

# *args(unpacking)(가변변수)
def args_func(*args): #매개변수 명은 자유여서 *a이렇게 사용해도 되지만 보통은 args로 사용
    for i, v in enumerate(args): #i 는 인덱스 v는 값
        print('Result : {}'.format(i), v)
    print('------')

args_func('dsad', 30)

# **kwargs(unpacting)(dictionry unpacking)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------------')

kwargs_func(name1 ='lee', name2 = 'kim', name3 = True)

#전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'lee', 'kim', name = 'ahn', name2 ='What')

#중첩함수

def nested_func(num):#2
    def func_in_func(num):#5
        print(num)
    print("In func")#3
    func_in_func(num + 100)#4
nested_func(100)#1

#람다식 예제
#메모리 절약, 가독성 항상, 코드 간결
#함수는 객체 생성 -> 리소시(메모리) 할당
#람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
#남발 시 가돗성 오히려 감소 

def mul_func(x,y):
    return x * Y

lamda_mul_func = lambda x, y : x*y

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x , y : x* y)