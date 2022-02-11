# Chapter02-1
#파이션 완전 기초
# print 사용법

#자주 쓰는 것 
print("Python Start")
print('Python Start')

#자주 쓰이지는 않는다
print('''Python Start''')
print("""Python Start""")

#seperator 옵션
print('P','Y','T',"H","O","N",sep="") 
print ("010","7777","1234",sep="-")

#end 옵션

print("Welcome to",end ="    ")
print("New World",end="!!!!")
print("Congrat")

#file 옵션
import sys

print("Learn Python", file=sys.stdout)#sys.stdout은 콘솔을 의미

#format 사용(d =interger, s=string , f=flaot) 중요도 (******)
print("%s %s" % ("one", "two"))
print("{} {}".format("one", "two"))# 위의 거와 똑같은 출력
print('{1} {0}'.format('one','two')) # 순서를 지정해 줄 수 있다


# %s
print("%10s" % ("nice"))#10개의 자리중에 오른쪽부터 채워지고 나머지는 공백으로 처리 
print('{:>10}'.format('nice'))#위에랑 똑같은 출력

print("%-10s" % ("nice"))#왼쪽 정렬 
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))# 부등호 앞에 있는것으로 공백의 대체

print('{:^10}'.format('nice'))
print('{:10.5}'.format('nicetry ahn'))#10개의 공간중 5개만 출력 
# %d랑 %f도 비슷함 
