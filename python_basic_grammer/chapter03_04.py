#chapter03_04
#Tuple
#리스트와의 비교 중요
#튜플자료형(순서 0, 중복0, 수정X, 삭제X) #불변  중요한 값들 변경해서는 안되는 값들 

a = ()
b = (1,) #원소가 하나일때는 뒤에 콤마를 붙어야 튜플로 인식함
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Capthine')
e = (100, 1000, ('Ace', 'Base', 'Capthine'))

#indexing 가능
print(d[1])
print(e[-1])

#수정 X
#d[0] = 1500 에러 발생

#슬라이싱
print(e[2][1:])

#튜플 연산
"""
+ 
*
"""

#튜플 함수 
a = (3, 1, 2, 5, 6)
print(a.count(1))

###중요 팩킹 & 언팩킹(Packing & Unnpacking)

#Packing

t = ('foo', 'bar', 'baz', 'quz')
#Unpacking
(x1, x2, x3, x4) = t

print(x1, x2, x3, x4)

#packing &unpacking 
t2 = 1, 2, 3 #괄호 생략 가능
t3 = 4,
x1, x2, x3  = t2
print(t2)
print(x1,x2,x3)