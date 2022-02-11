# 로그 파일 재정령 

# 로그의 가장 앞 부분은 식별자다.
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다
# 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
# 숫자 로그는 입력 순서대로 한다. 

def logfile(logs :list[str]) ->list :
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): # split()함수를 이용하면 공백마다 끊어준다. 
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key= lambda x : (x.split()[1], x.split()[0])) # sort 함수의 key를 이용하면 key 값으로 sort된다. 

    return print(letters + digits)

    pass


logs = ["dig1 3 2 4 2", "dig3 doadad dadas dasdsa"]

logfile(logs)