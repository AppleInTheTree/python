#Chapter04_02
#For 실습

#for in <collection>
#   <loop body>

from curses.ascii import isupper


for v1 in range(10):
    print('v1 is :', v1)

for v2 in range(1, 11): #1 ~10
    print('v2 is :', v2)

for v3 in range(1,11,2): #1~10 까지 2덧샘로 
    print('v3 is :', v3)

#1~ 1000까지의 합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1~1000 sum :', sum1)
#한줄로 sum 구하기 
print('1 1000까지의 4의 배수 :', sum(range(4,1000,4)))

# Iterables 자료형 반복(for에서 사용 가능)
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterable 리턴 함수 : range, reversed enumerate, filter, map, zip

#ex1)
names =['Kim', 'Park', 'Cho', 'Lee']

for n in names:
    print('your name is', n)

#ex2)
lotto_numbers = [11, 19, 21, 28, 28, 37]

for n in lotto_numbers:
    print("Current Number", n)

#ex3) 문자열로 iterable하기 떄문에 가능
word ='ejahn'

for s in word:
    print(s)


#ex4) dic
my_info = {
    "name" : 'Lee',
    "Age" : 25,
    "City" : 'Wonju'
}

for n in my_info:
    print(my_info[n])

for v in my_info.values():
    print('value', v)

#ex5) for and if

name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper)

#break

number = [14, 3, 4, 5, 213, 21, 321, 32, 34]

for n in number:
    if n =='34':
        print('Found')
        break
    else:
        print('Not Found')

#continue

#for-else # loop가 break가 없고 끊기지 않고 다 돌았을때 else 구문실행

number = [14, 3, 4, 5, 213, 21, 321, 32, 34]

for num in number:
    if num == 5:
        print('Found')
        break
else:
    print('Not Found')


#구구단 출력
for n in range(2,10):
    for m in range(1,10):
        print('{:4d}'.format(n*m), end =' ' )
    print()

name2 = 'Aceman'

print('Reversed', reversed(name2))

print('List', list(reversed(name2)))
print('Set', set(reversed(name2))) #순서 X 실행할때마다 다르게 나옴