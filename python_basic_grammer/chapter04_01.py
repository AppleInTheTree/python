#chapter04_01
#파이션 제어문 
#if 문

#기본 형식

print(type(True))# 0이 아닌수 , "abc", 리스트 튜플
print(type(False))# 0,"",[], {},()

#ex1
if True:
    print('Good')
else:
    print('Good')

#산술 > 관계 > 논리 순으로 연산된다

#중첩 if 문
grade = 'A'
total = 95
if grade == 'A':
    if total >=90:
        print('장학금 100%')
    elif total >=80:
        print('장학금 80%')
else:
    print('장학금 없음')

q = [10,20,30]
w = {
    'name' : 'Ahn',
    'city' : 'wonju'
}
q = {10, 20, 30}
r = (10,1214)
print("wonju" in w.values())