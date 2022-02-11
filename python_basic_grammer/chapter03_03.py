#chapter03_03
#리스트 사용법
#자료구조에서 중요 
#리스트 자료형 (순서0, 중복0, 수정0, 삭제0)가 가능한 유일한 자료형

#선언 
a = []
b = list()
c = [70, 80, 50, 20]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 100000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.131231]

#indexing (원하는 값을 꺼내오는 과정)

print()
print(type(d),d)
print(d[1])

print(e[-1][2])
print(list(e[-1][2]))

#Slicing 

print(e[2][0:2])

#list 연산

print('c + d = ', c + e)
print("'test' + c [0] = ",'test' + str(e[0]))

#값비교
print(c == c[:3] + c[3:])

#id
temp = c
print(id(temp), id(c))

#리스트 수정, 삭제
c[0] = 4
c[1:2] = ['a', 'b', 'c'] #슬라이싱으로 하면 원소만 들어가고 [[]]중첩을 해주면 리스트로 들어간다.
c[1] = ['a', 'b', 'c'] #인덱스로 이용하면 바로 리스트로 들어간다.
c[1:3] = []
del c[3] #자릿수에 있는 원소 삭제

#리스트 작성 함수
a = [5, 2, 1, 3, 4]
a.append(10)# 끝에 원소 추가
a.sort()# 오름차순 
a.reverse()# 역순 
a.insert(2, 7)# 3번쨰 자리에 7을 넣어라
a.remove(10) # 원하는 원소값 제거
a.pop()# 가장 뒤에 함수 사용
a.count(4) #원하는 원소값의 개수 반환
ex = [1,2,3]
a.extend(ex) #리스트를 원소로 마지막에 추가 
print(a)