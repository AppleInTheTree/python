#주어진 문자열이 팰린드롬인지 확인하라. 대소문자 구분 x 영문자와 숫자만 대상
#.isalnum 영어 숫자면 True



from collections import deque
import collections
from typing import Deque
import re
s = ' A man, a plan, a canal: Panama'
strs : Deque = collections.deque()

def paindrome(a):
    for i in s:
        if i.isalnum():
            strs.append(i.lower())
    print(strs)

    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False
        else:
            return True 

a =  paindrome(s)

print(a)

#deque 리스트랑 비슷하지만 양방향 큐이다. 양쪽 방향에서 append와pop이 가능

#슬라이싱과 정규식 이용
def isPalindrom(s : str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]

c = isPalindrom(s)
print(c)
                              