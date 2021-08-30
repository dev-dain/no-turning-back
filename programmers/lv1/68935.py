# 08-04
# https://programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기

def solution(n):
    s = ''
    while n:
        s += str(n % 3)
        n //= 3
    return int(s, 3)
