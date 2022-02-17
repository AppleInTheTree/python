def pl_dentence(n : str) ->str:
    res =[]
    s = n.split()
    for word in s:
        if word[0] in 'aeiou':
            res.append(f'{word}way')
        else:
            res.append(f'{word[1:0]}{word[0]}ay')
    return ''.join(res)
    