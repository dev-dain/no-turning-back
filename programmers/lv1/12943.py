# 08-03
# https://programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측
# 입력 : int
# 출력 : int

def solution(num):
    if num == 1: return 0
    counter = 0
    while num != 1 and counter < 500:
        if num % 2 == 0: num /= 2
        else: num = (num * 3) + 1
        counter += 1
    if num == 1: return counter
    return -1