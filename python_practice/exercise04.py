#16진수를 10진수로 반환

def hex_output():
    decnum = 0
    hexnum =input("Enter the hex number to convert : ")

    for power, digit in enumerate(reversed(hexnum)):
        decnum +=int(digit, 16) * (16 ** power)
        
    print(decnum)

hex_output()
