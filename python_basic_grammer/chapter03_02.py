#chapter03_02
#문자형
#문자형 중요

#문자열 생성
from platform import python_branch
from xmlrpc.server import SimpleXMLRPCRequestHandler


str1 ="I am Python"

print(len(str1))#len 문자열 숫자를 반환

#빈 문자열
str_t2 = ""
str_t1 = str() #위에랑 똑같다

print(type(str_t1), len(str_t1))

#이스케이프 문자사용
# \ \n(줄바꿈) \t(탭)
print('i/\'m boy') #\뒤에 문자도 출력 해줌

#raw string 
raw_s1 =r'D:\python\test' #\를 신경쓰지 않고 출력 해준다
print(raw_s1)

#멀티라인 입력
# \ 사용
multi_str = \
    '''
    hi
    hello
    hey
    '''
multi_str2 =\
    'hi'\
    'hello'
print(multi_str, multi_str2)

#문자열 연산
#in 연산자 사용 가능 시퀀스기 떄문에 

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print('y' in str_o1)
print('P' not in str_o1) #in 과 not in은 대소문자 구문

#문자열 형 변환
print(str(66),type(str(66)))
print(str(True),type(str(66)))

#문자열 내장 함수 (upper, isalnum, startswith, count endswith, isalpha, ...)

print("Capitalize : ", str_o1.capitalize())
print("endswith? : ", str_o1.endswith('s'))# 문단 끝에 있는 문자 확인
print("replace =", str_o1.replace('python', 'Hello')) 
print("sorted", sorted(str_o1)) #정열
print("split =", str_o3.split(' '))# 기준을 잡아 리스트로 분리

#시퀀스
im_str = "Good boy!"

print(dir(im_str)) #__iter__가 있다면 반복가능

#슬라이싱 연습 !!!!!

str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3])
print(str_s1[5 :]) # [5:11]
print(str_s1[:len(str_s1)])
print(str_s1[1:4:2])# 1에서 3까지 두개씩 뛰여서 가져온다
print(str_s1[1:-2]) #항상 두번째 인자에서 -1까지나온다
print(str_s1[::2])
print(str_s1[::-2])#역으로 출력

#아스키 코드 
a = "z"

print(ord(a))#아스키 값 반환
print(chr(122))#문자로 반환
