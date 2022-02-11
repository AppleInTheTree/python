#chapter04_03
#While

# whlie <expression>
#   <statement(w)>

#ex1)

n = 5
while n > 0:
    n = n -1
    print(n)


#무한반복 

a = ['foo', 'bar', 'dsa']

while True:
    if not a:
        break
    print(a.pop())



