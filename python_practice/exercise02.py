#Exerxise02 숫자 더하기


#sum[1,2,3] = 6 
#sum 함수를 만들어라

#case1
def mysum(s: list[int]):
    sum  = 0

    for i in s:
        sum+= i
    print(sum)
    return sum
    

v = mysum([1,2,3,4,5])
#case2

def mysum_s(*number): # 여러개의 매개변수를 받아온다
    sum  = 0

    for i in number:
        sum+= i
    print(sum)
    return sum


b =mysum_s(10,230,3,432,3)

print(b)

# case 3 : 평균을 구한다. 
# def mysum(s: list[int]):
#     sum  = 0
#     ls = len(s)

#     for i in s:
#         sum+= i
#     print(sum)
#     return sum//ls
    

# v = mysum([1,2,3,4,5])
# print(v)