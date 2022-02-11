#Chapter02-02
#파이션 완전 기초
#파이션 변수

#기본 선언
n = 700

print(n)
print(type(n))

#동시선언 가능

x=y=z=700
print(x,y,z)

#Object References
#변수 값 할당 상태
#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력

#ex)1
print(300)
print(int(300))

#ex2
n = 777
print(n, type(n))

#id(identify)확인 :  객체의 고유값 확인 (주소값)
n = 300
m = 400
print(id(n), id(m))#각 객체마다 고유의 주소값 할당

x = 300
z = 300
print(id(x), id(z))#같은 객체라면 여러개의 객체가 아니라 하나의 객체만 만들어지고 그 주소값을 참조

#다양한 변수 선언
#Camel Case : 소문자시작 -> Method 선언 할떄
#Pascal Case : 대문자시작  -> Class 선언 할때
#Snake Case : snake_case -> 파이션에서 변수를선언할때 

