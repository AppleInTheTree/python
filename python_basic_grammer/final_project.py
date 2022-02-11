import time 

#처음 인사

name = input('What is your name :')

print('Hi' + name, "Time to play hangman game")

print()

time.sleep(1)

print("Start Loading...")

time.sleep(0.5)

#정답 단어
word= 'secret'

#추츶 단어
guesses= ''

#기회
turns = 10

#핵심 While Loop
#찬스 카운트가 남아 있을 경우
while turns > 0:
    #단어 매치 수
    failed = 0

    #정답 단어 반복
    for char in word:
        #정답 단어 내에 추츶 문자가 포함되어 있는 경우
        if char in guesses:
            print(char, end='')
        else:
            print("_")
