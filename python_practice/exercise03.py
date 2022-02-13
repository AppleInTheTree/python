# Exercise03. 달린 시간 계산하기 

from queue import Empty


def run_timing():

    count = 0
    total_time = 0

    while True :
        run = input("10Km를 뛴 시간을 적으세요. : ")
        if not run :
            break
        total_time += int(run)

        count += 1
    return print("Average time is {} for {} run".format((total_time/count), count))


run_timing()