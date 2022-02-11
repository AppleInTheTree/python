# 숫자 맞추기 게임

#guessing_game 이라는 매개변수없는 함수
#0 ~100까지의 램덤한 숫자
# 숫자 입력 요구
# 사용자의 입풋에 따라 Too high or Too low or Just right 
# 예측 기회 3번 
import random
"""
import random
number = random.radint(10 , 30)
"""
def guessing_number():
    
    
    random_n = random.randint(0, 100)
    
    
    res = 0
    while(True):
        if res == 3:
            print("Failed")
            break
        number = int(input("숫자를 입력하세요 : "))

        if number == random_n :
            print("Just Right")
            break
        elif number >= random_n :
            print("Too high")
            res += 1
            pass
        else:
            print("Too low")
            res += 1
            pass

#guessing_number()

#guessing str from word list
def gussing_str():
    while(True):
        
        word_list = ["ho", "hi", "hello", "go"]
        anw = "hi"
        
        print(word_list)
        
        guess_w = input("Type a word from word list : ")
        
        if guess_w == anw:
            print("correct")
            break
        else:
            if guess_w == "ho":
                print("look lower")
            else:
                print("look high")

#gussing_str()
