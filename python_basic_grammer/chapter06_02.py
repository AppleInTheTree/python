#chapter06_02
# module
# module : 함수, 변수, 클래스 등 파이썬 구성 요소 들을 모야놓는 파일 


def add(x,y):
    return x + y 

def substart(x, y):
    return x -y 

def multifly(x, y):
    return x * y 

def divide(x, y):
    return x / y 

def power(x, y):
    return x ** y


# __name__ 사용 -> 다른곳에서 임포트 할경우에는 사용하지 않는다 
if __name__ == "__main__":
    print("inner called")