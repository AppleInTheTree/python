#chapter03_06
#set 집합
#set 자료형 (순서x, 중복x)

#선언

a = set()
print(type(a))
b =set([1,2,3,4])
e = {'foo', 'bar', 'baz', 'quz'}#딕셔녀리에 값이 없으면 집합으로 선언 가능
c = set([1,2,3,4])
d = set([2,3,4,5])
#집합 함수
print('c & d' , c & d)#교집합 same as c.intercection(d)

print('c | d', c.union(d))#합

print('c - d', c.difference(d))#차

"""
.isdisjoint() -> 중복되는 원소가 없나 false 가 나와야지 있는거
.issubset() -> 부분집합 확인 

"""

#추가
a.add(5)
a.remove(5)

a.discard(7)#remove와 같지만 예외발생하지 않음
a.clear()#다 지운다