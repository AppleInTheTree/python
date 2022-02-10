# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 
# 대소문자 구분을 하지 않으며, 구두점 또한 무시한다. 
import collections
from typing import Counter

import re
def most_common_word(paragraph : str, banned : list[str]) -> str:
    
    
    i=[]
   

    for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
    paragraph = paragraph.lower().split()
    
    print(paragraph)
    for words in paragraph:
        if words not in banned:
            i.append(words)
    print(i)
    counts  =collections.Counter(i)
    print(counts)
    return counts.most_common(1)[0][0]

s ="Hi, Mt dada dsa w s s w w a s"
ban = ["s"]
res = most_common_word(s, ban)

print(res)

