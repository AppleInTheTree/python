#chapter03_05
#dictionary
#범용적으로 가장 많이 사용
#딕셔너리 자료형(순서 X, 키 중복 X, 수정 0, 삭제 0) #사전을 예로들어 같은 단어가 두개일 수 없다. 

#선언

a = {'name' : 'Ahn', 'phone' : '01085244975', 'birth' : '981202'}
b = {0 : 'Hello python'}
c = {'arr' : [1,2,3,4]}
d = {
    'Name' : 'Ahn',
    'City' : 'Wonju',
    'Age' : 35,
    'Grade' : 'b+',
    'Status' : True
}

e = dict([
    ('Name',  'Ahn'),
    ('Age', 25)
])
#자주 하는 선언
f = dict(
    Name = 'Ahn',
    City = 'Wonju',
    Age = 25,
    Status = True
)

print('a -', type(a),a)
print('b -', type(b),b)
print('c -', type(c),c)
print('d -', type(d),d)
print('f -', type(f),f)

print('a -', a['name'])
print('a -', a.get('name1'))#get으로 접근 하면 키가 없을경우 None으로 출력 안전하다 
print('b -', b[0])
print('b -', b.get(2))

#딕셔너리 길이 
a['address'] = 'seoul'
print('a -', a)

print('a -', len(a)) #키의 개수의 샌다.

#dict_keys, dict_values, dict_items : 반복문에서 사용 가능 

print('a -', list(a.keys()))
print()
print('d -', d.values())
print()
print('d -', d.items())#키와 값이 튜플로 변환

print('a -', a.pop('name'))#pop으로 출력한다음 그 값의 없앤다. 
print('a -', a.popitem())#임의로 하나의 키와 값을 출력한다음 제거 
print()
#in 연산자
print('a -', 'age' in a)# 키를 포함할수 있는지 확인 할 수 있다

#수정

a.update(birth = '9812')
print(a)
temp = {'address' : 'Wonju'}
a.update(temp)
print(a)