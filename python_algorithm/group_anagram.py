# 49.Group Anagram

"""
Input : [eat, tea, tan, ate, nat, bat]
Ouput : [
    [ate, eat, tea]
    [nat, tan]
    [bat]
]
"""

#defualt dict은 딕셔너리의 초기값을 그 해당 괄호에 있는 변수로 선어내준다
#sorted() 함수는 값을 list 형식으로 반환하기 때문에 ''.join(sorted())를 해주어 단어를 붙여준다.

# ex) res =collections.defualtdick(list)

from collections import defaultdict
import collections
def groupAnagrams(strs : list[str]) ->list[list[str]]:

    anagram = collections.defaultdict(list)

    for a in strs:
        anagram[''.join(sorted(a))].append(a)
    return anagram.values