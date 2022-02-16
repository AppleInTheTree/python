# 피그 라틴 단어 만들기 

def figLatin(n : str) -> str:
    way = ['a', 'e', 'i', 'o', 'u']
    
    if n[0] in way:
        return f'{n}way'
    else:
        return f'{n[1:]}{n[0]}ay'

print(figLatin('python'))


    
    