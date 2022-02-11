#chapter03_01
#숫자형

#파이션 지원 자료형
"""
int : 정수 
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

#데이터 타입
from tkinter import Y


str1 = "python"
bool = True
str2 = "Ancaconde"
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2.0

}
tuple = (6, 5, 7) #괄호가 없어도 인식함 6, 5, 7
set ={1, 2, 3}

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자

"""
+
-
*
// : 몫
%
abs(x) : 절대값
pow(x,y) : 제곱 == x**y

"""

#형 변환 실습

a = 3.
b = 6
c = .7
d = 12.7
#타입 출력
print(type(a),type(b),type(c),type(d))
#형 변환
print(float(a))
print((int(c)))
print(int(True)) # True : 1, False: 0
print(complex(3))

#수치 연산 함수
print(abs(-7))
x, y = divmod(100,8) #divmde 몫과 나머지로 할당
print(pow(5,3), 5**3)

#외부 모듈 -> 나중에 설명
import math

print((math.pi))
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 

print(type(0))
