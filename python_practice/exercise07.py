# exercise07 비밀 언어 우비두비 단어 만들기
# auiou 앞에 ub를 붙힌다. milk -> mubuilk

def ubbi_dubbi(s : str) -> str:
    output = []

    for letter in s:
        if letter in 'aueio':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    
    return ''.join(output)

print(ubbi_dubbi('python'))

